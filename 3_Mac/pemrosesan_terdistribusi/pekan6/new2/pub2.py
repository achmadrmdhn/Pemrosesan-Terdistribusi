import zmq
import time
import random

ctx = zmq.Context()
socket = ctx.socket(zmq.PUB)
socket.bind("tcp://*:5557")  # Port berbeda

while True:
    msg = f"kelembapan {random.uniform(60, 90):.2f}"
    print(f"[PUB2] {msg}")
    socket.send_string(msg)
    time.sleep(1.5)

