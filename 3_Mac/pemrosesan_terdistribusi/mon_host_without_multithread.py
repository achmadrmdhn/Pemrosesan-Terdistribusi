import os
import time
from datetime import datetime

print(f"Mulai: {datetime.today()}")
with open('3_Mac/host.cfg') as hosts:
   host = hosts.read().split()
   for h in host:
      cmd = os.popen(f"ping -c 3 {h}")
      res = cmd.read()
      status = 'MATI'
      if res.find("3 received") >= 0:
         status = 'HIDUP'
      print(f"Server {h} : {status}") 
print(f"Selesai: {datetime.today()}")
