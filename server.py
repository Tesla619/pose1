import asyncio
import cv2
import numpy as np
import websockets

async def video_feed(websocket, path):
    cap = cv2.VideoCapture(1)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Convert the frame to bytes
        _, buffer = cv2.imencode('.jpg', frame)
        data = buffer.tobytes()

        # Send the frame over the websocket
        await websocket.send(data)        
        
        print("working")


    cap.release()

# Start the websocket server
start_server = websockets.serve(video_feed, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

# & C:/Users/User/.conda/envs/tfv2/python.exe c:/Users/User/Desktop/Thesis/pose1/client.py