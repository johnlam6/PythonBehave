import json
import time
from behave import given, when, then
from utils.ws_client import WebSocketClient

@given("WebSocket connection is established")
def step_connect(context):
    context.ws = WebSocketClient("wss://stream.crypto.com/exchange/v1/market")
    context.ws.connect()

@when('I subscribe to "{channel}"')
def step_subscribe(context, channel):
    context.channel = channel
    subscribe_payload={
        "id": 1,
        "method": "subscribe",
        "params": {
            "channels": [channel]
        }
    }
    context.ws.send_json(subscribe_payload)

    context.ws_send = subscribe_payload

    context.response = context.ws.receive_json(timeout=5)
    context.ws_ack = context.response

@then("I should receive a snapshot response")
def step_receive_snapshot(context):
    import json

    # Validate ACK
    assert context.response.get("code") == 0, f"Subscription failed: {context.response}"
    assert "channel" in context.response, "No 'channel' in ACK"
    assert context.response["channel"].startswith("book"), f"Unexpected channel {context.response['channel']}"

    # Initialize the list to store all messages
    messages = []

    # Wait for snapshot: loop until we get a message containing "result" with "data"
    snapshot = None
    max_retries = 5

    for attempt in range(max_retries):
        message = context.ws.receive_json(timeout=5)
        print(f"Message {attempt + 1}:", json.dumps(message, indent=2))

        if (
            message.get("method") == "subscribe"
            and message.get("code") == 0
            and "result" in message
            and "data" in message["result"]
        ):
            snapshot = message["result"]
            break

    assert snapshot is not None, "Did not receive a valid snapshot with order book data"
    context.snapshot = snapshot

    context.ws_messages = messages # Save all messages

@then("the snapshot should contain 10 bids and 10 asks")
def step_validate_depth(context):
    import json

    # Loop until we get a snapshot with 'result' and 'data'
    snapshot = None
    for _ in range(5):  # Retry up to 5 times
        message = context.ws.receive_json(timeout=5)
        print("Received message:", json.dumps(message, indent=2))

        if (
            message.get("method") == "subscribe"
            and message.get("code") == 0
            and "result" in message
            and "data" in message["result"]
        ):
            snapshot = message["result"]
            break

    assert snapshot is not None, "Valid snapshot with 'result' and 'data' not received"
    data = snapshot["data"][0]

    assert "bids" in data, "Missing 'bids'"
    assert "asks" in data, "Missing 'asks'"
    assert len(data["bids"]) == 10, f"Expected 10 bids, got {len(data['bids'])}"
    assert len(data["asks"]) == 10, f"Expected 10 asks, got {len(data['asks'])}"

@then("I should receive an error response")
def step_error_response(context):
    assert context.response["code"] != 0