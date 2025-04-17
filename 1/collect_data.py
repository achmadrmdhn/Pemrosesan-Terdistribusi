import requests
from bs4 import BeautifulSoup
from datetime import datetime

web_list = ["www.detik.com","www.kompas.com","www.cnn.com",
           "www.nurulfikri.ac.id","www.republika.co.id",
           "www.facebook.com","www.yahoo.com",
           "elena.nurulfikri.ac.id","siska.nurulfikri.ac.id"
           ]

def getweb(url):
    req = requests.get(f"https://{url}")
    page = BeautifulSoup(req.text,'html.parser')  
    if page.title:
       return page.title.text
    return ''

print(datetime.today())
for web in web_list:
    hasil = getweb(web)
    print(hasil)
print(datetime.today())
