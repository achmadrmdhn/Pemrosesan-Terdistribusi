#File Name : rpcserver.py
import rpcserver
import os
class MyRPC(object):
        def greetings(self):
                return "Hello World"
        def hostname(self):
                return os.popen('hostname').read()
s = rpcserver.Server(MyRPC())
s.bind("tcp://0.0.0.0:4242")
s.run()