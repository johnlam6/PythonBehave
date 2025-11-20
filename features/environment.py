import os
import json
from datetime import datetime
from behave.log_capture import capture

@capture
def after_scenario(context, scenario):
    os.makedirs("logs", exist_ok=True)
    log_file = "logs/test_log.txt"

    feature_file = scenario.feature.filename
    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    request_url = getattr(context, "request_url", "N/A")
    response = getattr(context, "response", None)

    with open(log_file, "a", encoding="utf-8") as f:
        f.write("=" * 80 + "\n")
        f.write(f"Timestamp: {timestamp}\n")
        f.write(f"Feature: {os.path.basename(feature_file)}\n")
        f.write(f"Scenario: {scenario.name}\n")
        f.write(f"Status: {scenario.status}\n\n")

        # If this is an API test
        if "get_candlestick.feature" in feature_file:
            if response:
                f.write("Request URL:\n")
                f.write(f"{request_url}\n\n")

                f.write("Response:\n")
                try:
                    if hasattr(response, "json"):
                        json_data = response.json()
                        f.write(json.dumps(json_data, indent=2, ensure_ascii=False) + "\n\n")
                    else:
                        f.write(json.dumps(response, indent=2, ensure_ascii=False) + "\n\n")
                except Exception:
                    f.write(str(response) + "\n\n")

        # If this is a WebSocket test
        if "book_subscription.feature" in feature_file:
            if hasattr(context, "ws_send"):
                f.write("WebSocket Sent:\n")
                f.write(json.dumps(context.ws_send, indent=2, ensure_ascii=False) + "\n\n")

            if hasattr(context, "ws_ack"):
                f.write("WebSocket ACK Response:\n")
                f.write(json.dumps(context.ws_ack, indent=2, ensure_ascii=False) + "\n\n")

            if hasattr(context, "ws_messages"):
                f.write("WebSocket Messages:\n")
                for idx, msg in enumerate(context.ws_messages, 1):
                    f.write(f"Message {idx}:\n")
                    f.write(json.dumps(msg, indent=2, ensure_ascii=False) + "\n\n")

            if hasattr(context, "snapshot"):
                f.write("Snapshot Data:\n")
                f.write(json.dumps(context.snapshot, indent=2, ensure_ascii=False) + "\n\n")
