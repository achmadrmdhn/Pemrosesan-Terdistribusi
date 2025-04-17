import zmq

ctx = zmq.Context()
socket = ctx.socket(zmq.SUB)

# Connect ke semua publisher
socket.connect("tcp://localhost:5556")
socket.connect("tcp://localhost:5557")

# Subscribe ke semua topik
socket.setsockopt_string(zmq.SUBSCRIBE, "suhu")
socket.setsockopt_string(zmq.SUBSCRIBE, "kelembapan")

print("Subscriber connected to multiple publishers...")

while True:
    msg = socket.recv_string()
    print(f"[SUB] Received: {msg}")

