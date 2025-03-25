import zerorpc

class MyRPC(object):
  def luas(self, panjang, lebar):
    return panjang * lebar
  
  def keliling(self, panjang, lebar):
    return (panjang * 2) + (lebar * 2)

s = zerorpc.Server(MyRPC())
s.bind("tcp://0.0.0.0:4242")
s.run()