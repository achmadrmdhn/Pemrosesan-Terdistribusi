import zmq
# ZeroMQ Context
context = zmq.Context()
# Define the socket using the "Context"
sock = context.socket(zmq.SUB)
# Define subscription and messages with prefix to accept.
sock.setsockopt(zmq.SUBSCRIBE, b"Temperature")
# sock.connect("tcp://192.168.55.210:5556")
sock.connect("tcp://127.0.0.1:5556")
while True:
    message= sock.recv()
    print(message.decode())