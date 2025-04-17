import os
import time
from datetime import datetime
import multiprocessing

def ping(h):
      cmd = os.popen(f"ping -c 3 {h}")
      res = cmd.read()
      status = 'MATI'
      if res.find("3 received") >= 0:
         status = 'HIDUP'
      print(f"Server {h} : {status}") 

print(f"Mulai: {datetime.today()}")
with open('2/host.cfg') as hosts:
   host = hosts.read().split()
   t_list = []
   for h in host:
       t = multiprocessing.Process(target=ping, args=[h])
       t_list.append(t)
       t.start()
   for t in t_list:
       t.join()
print(f"Selesai: {datetime.today()}")
