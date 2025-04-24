import redis
import itertools
import json
from config import QUEUE_NAME

r = redis.Redis(host='192.168.99.214', port=6379, db=0)

# Set karakter dan panjang password
chars = 'abcdefghijklmnopqrstuvwxyz'
max_length = 4  # Contoh: semua kemungkinan 1-4 huruf

def generate_combinations():
    for length in range(1, max_length + 1):
        for combo in itertools.product(chars, repeat=length):
            yield ''.join(combo)

for password in generate_combinations():
    r.rpush(QUEUE_NAME, json.dumps({"password": password}))

print("Semua kemungkinan telah dikirim ke antrian.")

