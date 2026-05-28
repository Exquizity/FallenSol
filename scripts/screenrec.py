import cv2
import numpy as np
import mss
import time
import os

def start_recording(curbiome):
    record_time = 0
    if curbiome.lower() == "glitched":
        record_time = 170
    else:
        record_time = 200
    filename = f"{curbiome.upper()}.mp4"

    print(f"Recording {curbiome.upper()} for {record_time}s...")

    with mss.mss() as sct:
        monitor = sct.monitors[1]
        vid = cv2.VideoWriter(filename, cv2.VideoWriter_fourcc(*"mp4v"), 30, (1280, 720))

        start = time.time()
        while time.time() - start < record_time:
            frame = np.array(sct.grab(monitor))
            frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)
            frame = cv2.resize(frame, (1280, 720))
            vid.write(frame)

        vid.release()
        print(f"Saved Recording: {os.path.abspath(filename)}")
