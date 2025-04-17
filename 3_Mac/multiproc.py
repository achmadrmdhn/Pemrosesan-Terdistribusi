import os
import time
from datetime import datetime
import multiprocessing

def ping(h):
    """Function to ping a host and check if it's alive."""
    try:
        # Adjust command based on OS
        if os.name == "nt":  # Windows
            cmd = os.popen(f"ping -n 3 {h}")
            success_indicator = "Received = 3"
        else:  # macOS/Linux
            cmd = os.popen(f"ping -c 3 {h}")
            success_indicator = "3 received"
        
        res = cmd.read()
        status = "MATI"
        if success_indicator in res:
            status = "HIDUP"
        
        print(f"Server {h} : {status}")
    
    except Exception as e:
        print(f"Error pinging {h}: {e}")

if __name__ == "__main__":  # ✅ Required for multiprocessing
    multiprocessing.set_start_method("spawn", force=True)  # ✅ Fix for macOS & Windows

    print(f"Mulai: {datetime.today()}")

    try:
        with open("3_Mac/host.cfg") as hosts:
            host_list = hosts.read().split()

        t_list = []
        for h in host_list:
            t = multiprocessing.Process(target=ping, args=(h,))
            t_list.append(t)
            t.start()

        for t in t_list:
            t.join()

    except FileNotFoundError:
        print("Error: File 'host.cfg' not found.")

    print(f"Selesai: {datetime.today()}")
