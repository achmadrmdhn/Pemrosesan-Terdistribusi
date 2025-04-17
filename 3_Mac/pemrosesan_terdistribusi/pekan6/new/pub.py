#Notifikasi Cuaca Real-Time
#Misalnya, kita sedang membangun sistem notifikasi cuaca real-time. Ada satu server pusat (Publisher) yang terus-menerus mengirimkan data cuaca (seperti suhu, kelembapan, kondisi cuaca), dan beberapa klien pengguna (Subscriber) yang hanya tertarik pada topik tertentu, misalnya hanya data suhu atau kelembapan.

#Struktur:
#Publisher: Mengirimkan pesan dengan topik (misal: "suhu", "kelembapan").
#Subscriber: Menerima hanya pesan dengan topik yang mereka minati.
#Cara Menjalankan:
#   Jalankan publisher.py di satu terminal.
#   Jalankan subscriber.py di satu atau lebih terminal lain (ubah topic_filter untuk mencoba berbagai topik).

import zmq
import time
import random

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5555")

topics = ["suhu", "kelembapan", "cuaca"]

while True:
    topic = random.choice(topics)
    value = round(random.uniform(20.0, 40.0), 2)
    message = f"{topic} {value}"
    print(f"Publishing: {message}")
    socket.send_string(message)
    time.sleep(1)





