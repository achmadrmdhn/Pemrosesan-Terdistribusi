import os
import time
from datetime import datetime
import multiprocessing
import platform

def ping(h):
    system = platform.system()
    if system == "Windows":
        cmd = f"ping -n 3 {h}"
    else:
        cmd = f"ping -c 3 {h}"

    result = os.popen(cmd).read()
    
    status = 'MATI'
    if "TTL=" in result or "3 received" in result:
        status = 'HIDUP'

    print(f"Server {h} : {status}")

def main():
    print(f"Mulai: {datetime.now()}")

    try:
        with open('2/host.cfg') as hosts:  # Pastikan file host.cfg ada di direktori yang benar
            host_list = hosts.read().split()
            
            process_list = []
            for h in host_list:
                p = multiprocessing.Process(target=ping, args=(h,))
                process_list.append(p)
                p.start()
            
            for p in process_list:
                p.join()
    except FileNotFoundError:
        print("File host.cfg tidak ditemukan. Pastikan file tersebut ada di direktori yang benar.")

    print(f"Selesai: {datetime.now()}")

if __name__ == "__main__":
    main()