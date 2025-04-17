import requests
from bs4 import BeautifulSoup
from datetime import datetime
import concurrent.futures
import time

web_list = [
    "www.detik.com", "www.kompas.com", "www.cnn.com",
    "www.nurulfikri.ac.id", "www.republika.co.id",
    "www.facebook.com", "www.yahoo.com",
    "elena.nurulfikri.ac.id", "siska.nurulfikri.ac.id"
]

def getweb(url):
    try:
        req = requests.get(f"https://{url}", timeout=5)  # Tambahkan timeout
        req.raise_for_status()  # Cek apakah ada error HTTP
        page = BeautifulSoup(req.text, 'html.parser')
        if page.title:
            print(f"{url}: {page.title.text}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
    time.sleep(1)  # Kurangi delay agar lebih cepat

print(datetime.today())

# Gunakan ThreadPoolExecutor untuk efisiensi
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    executor.map(getweb, web_list)

print(datetime.today())
