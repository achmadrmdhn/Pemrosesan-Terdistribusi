import redis
import hashlib
import json
import time
from config import TARGET_HASH, QUEUE_NAME, STOP_KEY

r = redis.Redis(host='192.168.99.214', port=6379, db=0)

print("Worker aktif. Mencoba memecahkan hash...")

while True:
    # Cek apakah password sudah ditemukan
    if r.exists(STOP_KEY):
        print("Password ditemukan oleh worker lain. Keluar.")
        break

    task_json = r.blpop(QUEUE_NAME, timeout=5)
    if task_json:
        _, data = task_json
        task = json.loads(data)
        pwd = task['password']
        hashed = hashlib.md5(pwd.encode()).hexdigest()

        if hashed == TARGET_HASH:
            print(f"[Ditemukan 🎉] Password = '{pwd}'")
            r.set(STOP_KEY, pwd)
            break
        else:
            print(f"[coba] {pwd} → {hashed}")
    else:
        print("Tidak ada task, worker idle...")
        time.sleep(2)

