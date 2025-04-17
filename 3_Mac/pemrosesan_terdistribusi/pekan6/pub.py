import zmq
import time
import random
# ZeroMQ Context
context = zmq.Context()
# Define the socket using the "Context"
sock = context.socket(zmq.PUB)
# sock.bind("tcp://192.168.55.210:5556")
sock.bind("tcp://127.0.0.1:5556")
while True:
    time.sleep(3)
    tmp, now = random.randrange(30,45), time.ctime()
    # Message [prefix][message]
    message = "Temperature-Update! >> #{tmp} Celcius >> {time}".format(tmp=tmp, time=now)
    sock.send(message.encode())
    hum, now = random.randrange(30,50), time.ctime()
    # Message [prefix][message]
    message = "Humidity-Update! >> #{hum} % >> {time}".format(hum=hum, time=now) 
    sock.send(message.encode())
