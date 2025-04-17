import streamlit as st
from datetime import datetime
import os
import requests
from bs4 import BeautifulSoup



# Fungsi untuk membaca daftar URL dari file
def baca_daftar_url(weblist_path):
    try:
        with open(weblist_path, 'r') as file:
            url_list = file.readlines()
        url_list = [url.strip() for url in url_list if url.strip()]  # Menghapus spasi kosong dan baris kosong
        return url_list
    except FileNotFoundError:
        st.error(f"File {weblist_path} tidak ditemukan.")
        return []

titles = {}
# Membuat fungsi ping
def get_title(url):
    req = requests.get(f"https://{url}")
    page = BeautifulSoup(req.text,"html.parser")
    titles[url] = ''
    if page.title:
        titles[url] = page.title.text
    return titles[url]

# File yang berisi daftar URL (gantilah path dengan lokasi file Anda)
weblist_path = "weblist.txt"

# Membaca daftar URL
daftar_url = baca_daftar_url(weblist_path)

# Judul aplikasi
st.title("Pengambilan title web")

# Menampilkan daftar URL dalam tabel
if daftar_url:
    st.write("Daftar URL web yang akan diambil title nya:")
    no = 1
    for url in daftar_url:
       st.write(f"{no}. {url}")
       no = no + 1
     

# Tombol untuk memulai ping
if st.button("Mulai Scraping"):
    # Membuat list untuk menampung hasil scraping
    hasil_ping = []
    st.write(f"Mulai : {datetime.today()}")
    for url in daftar_url:
        response = get_title(url)
    
        if not response:
            st.error(f"Gagal mendapatkan title dari {url}.")
        else:
            st.success(f"Title web {url} : {response}")
    st.write(f"Selesai: {datetime.today()}")
