print("python works")
import cv2
import numpy as np
import mss
import time
import os

def start_recording(curbiome):
    record_time = 5  # short test
    filename = f"{curbiome.upper()}.mp4"

    print("Step 1: Starting...")

    with mss.mss() as sct:
        print("Step 2: mss loaded")
        monitor = sct.monitors[1]
        print(f"Step 3: Monitor = {monitor}")

        width = monitor["width"]
        height = monitor["height"]

        out = cv2.VideoWriter(filename, cv2.VideoWriter_fourcc(*"mp4v"), 30, (width, height))
        print(f"Step 4: VideoWriter created, is opened: {out.isOpened()}")

        start = time.time()
        frames = 0
        while time.time() - start < record_time:
            frame = np.array(sct.grab(monitor))
            frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)
            out.write(frame)
            frames += 1

        out.release()
        print(f"Step 5: Done. Frames recorded: {frames}")
        print(f"Step 6: File saved to: {os.path.abspath(filename)}")

if __name__ == "__main__":
    start_recording("test")

input("Press enter to close")