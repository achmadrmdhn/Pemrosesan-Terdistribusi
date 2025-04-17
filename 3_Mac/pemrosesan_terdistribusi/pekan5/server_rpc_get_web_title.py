import zerorpc
import requests
from bs4 import BeautifulSoup
from datetime import datetime

class GetTitle(object):
    # Membuat fungsi/metod get_title
    def get_title(self,url):
        req = requests.get(f"https://{url}")
        page = BeautifulSoup(req.text,"html.parser")
        title = ''
        if page.title:
           title = page.title.text
        print(f"{datetime.today()}: RPC - Terjadi pemanggilan prosedur get_title({url})")
        return title

s = zerorpc.Server(GetTitle())
s.bind("tcp://0.0.0.0:4242")
s.run()

