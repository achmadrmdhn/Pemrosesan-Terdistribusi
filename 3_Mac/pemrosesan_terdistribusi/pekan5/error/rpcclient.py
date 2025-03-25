#File Name: rpcclient.py
import zerorpc
c = zerorpc.Client()
c.connect("tcp://127.0.0.1:4242")
print("Greetings: ",c.greetings())
print("Hostname: ",c.hostname())