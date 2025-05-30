import random
# Simulasi 3 node data
nodes = [{"val": 10}, {"val": 10}, {"val": 10}]
N =3
R = 2 # read quorum
W = 2 # write quorum
# Fungsi tulis dengan quorum
def write_value(value):
    write_nodes = random.sample(nodes, W)
    for node in write_nodes:
        node["val"] = value
    print(f"Write to nodes: {[node['val'] for node in nodes]}")
    

# Fungsi baca dengan quorum
def read_value():
    read_nodes = random.sample(nodes, R)
    values = [node["val"] for node in read_nodes]
    print(f"Read from nodes: {values}")
    return max(set(values), key=values.count)
write_value(20)
read_value()