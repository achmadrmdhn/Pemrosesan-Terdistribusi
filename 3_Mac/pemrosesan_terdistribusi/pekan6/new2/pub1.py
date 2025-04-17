import zmq
import time
import random

ctx = zmq.Context()
socket = ctx.socket(zmq.PUB)
socket.bind("tcp://*:5556")  # Port berbeda

while True:
    msg = f"suhu {random.uniform(20, 30):.2f}"
    print(f"[PUB1] {msg}")
    socket.send_string(msg)
    time.sleep(1)

