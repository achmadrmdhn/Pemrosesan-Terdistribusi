import zerorpc

rpc = zerorpc.Client()
rpc.connect("tcp://192.168.6.11:4242")
panjang = 20
lebar = 15

print(rpc.luas(panjang, lebar))
print(rpc.keliling(panjang, lebar))