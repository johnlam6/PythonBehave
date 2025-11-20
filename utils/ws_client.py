import websocket
import json

class WebSocketClient:
    def __init__(self, url):
        self.url = url
        self.ws = None

    def connect(self):
        self.ws = websocket.create_connection(self.url)

    def send_json(self, message):
        self.ws.send(json.dumps(message))

    def receive_json(self, timeout=5):
        self.ws.settimeout(timeout)
        data = self.ws.recv()
        return json.loads(data)

    def close(self):
        if self.ws:
            self.ws.close()