# subscriber.py
import zmq

context = zmq.Context()
socket = context.socket(zmq.SUB)

# Connect ke server
socket.connect("tcp://localhost:5555")

# Subscribe ke topik tertentu
topic_filter = "cuaca"  # Ubah ke "kelembapan" atau "cuaca" sesuai kebutuhan
socket.setsockopt_string(zmq.SUBSCRIBE, topic_filter)

print(f"Subscribed to topic: {topic_filter}")

while True:
    message = socket.recv_string()
    print(f"Received: {message}")

