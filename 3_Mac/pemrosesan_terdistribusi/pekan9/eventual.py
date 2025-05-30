import time
import threading
# Simulasi dua node dengan data
data_node_A = {"counter": 0}
data_node_B = {"counter": 0}
# Fungsi update di Node A
def update_node_A():
    data_node_A["counter"] += 1
    print("Node A update:", data_node_A["counter"])

# Sinkronisasi (replikasi) ke Node B
def replicate_to_B():
    while True:
        time.sleep(2)  # delay replikasi
        data_node_B["counter"] = data_node_A["counter"]
        print("Replikasi ke Node B:", data_node_B["counter"])
threading.Thread(target=replicate_to_B, daemon=True).start()
# Simulasi update
for _ in range(5):
    update_node_A()
    time.sleep(1)