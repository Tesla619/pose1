import asyncio
import cv2
import numpy as np
import time
import websockets

async def receive_frames():
    async with websockets.connect('ws://100.77.189.76:8765') as websocket:
        cap = cv2.VideoCapture(0)
        start_time = time.time()
        frames = 0

        while True:
            # Receive the frame from the websocket
            data = await websocket.recv()

            # Convert the bytes to a NumPy array
            buffer = np.frombuffer(data, dtype=np.uint8)

            # Decode the JPEG image
            frame = cv2.imdecode(buffer, cv2.IMREAD_COLOR)

            # Calculate the elapsed time and FPS
            elapsed_time = time.time() - start_time
            fps = frames / elapsed_time

            # Display the FPS counter on the image
            fps_text = f"FPS: {fps:.2f}"
            cv2.putText(frame, fps_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            # Show the image
            cv2.imshow('Frame', frame)
            
            # Close all windows when q pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):                
                break

            # Increment the frame counter
            frames += 1
            
        cv2.destroyAllWindows()

# Start the client to receive frames
asyncio.get_event_loop().run_until_complete(receive_frames())
