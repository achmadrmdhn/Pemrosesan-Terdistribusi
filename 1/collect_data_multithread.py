import requests
from bs4 import BeautifulSoup
from datetime import datetime
import threading

web_list = ["www.detik.com","www.kompas.com","www.cnn.com",
           "www.nurulfikri.ac.id","www.republika.co.id",
           "www.facebook.com","www.yahoo.com",
           "elena.nurulfikri.ac.id","siska.nurulfikri.ac.id"
           ]

def getweb(url):
    req = requests.get(f"https://{url}")
    page = BeautifulSoup(req.text,'html.parser')  
    if page.title:
       print(page.title.text)
    print()

print(datetime.today())
t_list = []
for web in web_list:
    t = threading.Thread(target=getweb,args=[web])
    t.start()
    t_list.append(t)

for t in t_list:
    t.join()

print(datetime.today())
