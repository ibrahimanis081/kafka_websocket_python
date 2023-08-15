# import asyncio
# import websockets
 
# host = "localhost"
# port = 8000

# async def handler(websocket, path):
 
#     data = await websocket.recv()
 
#     reply = f"Data recieved as:  {data}!"
 
#     await websocket.send(reply)
 
# start_server = websockets.serve(handler, host, port)
# asyncio.get_event_loop().run_until_complete(start_server)
# print(f"Websocket listening on host= {host}, port= {port} ")
# asyncio.get_event_loop().run_forever()

import asyncio
import websockets

host = "localhost"
port = 8000

connected_clients = set()

async def handler(websocket, path):
    # Add the client to the set of connected clients
    connected_clients.add(websocket)
    print("Client connected")

    try:
        while True:
            data = await websocket.recv()
            print(f"Received data: {data}")

            # Forward the message to all other connected clients
            for client in connected_clients:
                if client != websocket:
                    await client.send(data)
                    print(f"Message forwarded to a client")

    except websockets.exceptions.ConnectionClosedError:
        # If a client disconnects, remove it from the set of connected clients
        connected_clients.remove(websocket)
        print("Client disconnected")


start_server = websockets.serve(handler, host, port)
print(f"WebSocket listening on host={host}, port={port}")

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()