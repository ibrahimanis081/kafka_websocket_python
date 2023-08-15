import websocket

def on_message(ws, message):
    upper = str(message).upper()
    print(f"Received: {upper}")

def on_error(ws, error):
    print(f"Error: {error}")

def on_close(ws, close_status_code, close_msg):
    print("WebSocket closed")

def on_open(ws):
    print("Connected to WebSocket server")

if __name__ == "__main__":
    # Replace 'ws://your_websocket_server_url' with the actual URL of your WebSocket server
    websocket_url = 'ws://localhost:8000'

    # Create a WebSocket connection
    ws = websocket.WebSocketApp(websocket_url,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open

    # Run the WebSocket connection
    ws.run_forever()
