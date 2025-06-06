import os
import time
from datetime import datetime

print(f"Mulai: {datetime.today()}")
with open('2/host.cfg') as hosts:
   host = hosts.read().split()
   for h in host:
      cmd = os.popen(f"ping -c 3 {h}")
      res = cmd.read()
      status = 'MATI'
      if res.find("Received = 3") >= 0:
         status = 'HIDUP'
      print(f"Server {h} : {status}") 
print(f"Selesai: {datetime.today()}")