import socket
import threading
import time
import sys

ROLE = sys.argv[1] # "primary" atau "backup"
PORT = int(sys.argv[2])

BACKUPS = [("127.0.0.1", 9001), ("127.0.0.1", 9002)]
PRIMARY_PORT = 9000
HEARTBEAT_INTERVAL = 1
HEARTBEAT_TIMEOUT = 3

last_heartbeat = time.time()
is_primary = ROLE == "primary"

def handle_data_connection(conn, addr):
    global is_primary
    print(f"[{ROLE.upper()}] Koneksi data dari {addr}")
    while True:
        try:
            data = conn.recv(1024).decode()
            if not data:
                break
            print(f"[{ROLE.upper()}] Terima data: {data}")
            if is_primary:
                replicate_to_backups(data)
        except:
            break
    conn.close()

def replicate_to_backups(data):
    for ip, port in BACKUPS:
        if port == PORT:
            continue # Jangan kirim ke diri sendiri
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((ip, port))
                s.sendall(data.encode())
        except Exception as e:
            print(f" [PRIMARY] Gagal kirim ke backup {ip}: {port} - {e}")

def heartbeat_sender():
    while is_primary:
        for ip, port in BACKUPS:
            if port == PORT:
                continue
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.connect((ip, port + 100)) # Heartbeat port
                    s.sendall(b"HB")
            except:
                pass
        time.sleep(HEARTBEAT_INTERVAL)

def heartbeat_listener():
    global last_heartbeat
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', PORT + 100))
    s.listen()
    print(f"[{ROLE.upper()}] Mendengarkan heartbeat di port {PORT + 100}")
    while not is_primary:
        conn, addr = s.accept()
        with conn:
            data = conn.recv(1024)
            if data == b"HB":
                last_heartbeat = time.time()

def heartbeat_monitor():
    global is_primary
    while not is_primary:
        if time.time() - last_heartbeat > HEARTBEAT_TIMEOUT:
            print(f" [BACKUP: {PORT}] Primary tidak merespons! Promosi ke PRIMARY!")
            is_primary = True
            threading.Thread(target=heartbeat_sender, daemon=True).start()
            break
        time.sleep(1)

def data_listener():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', PORT))
    s.listen()
    print(f"[{ROLE.upper()}] Mendengarkan data di port {PORT}")
    while True:
        conn, addr = s.accept()
        threading.Thread(target=handle_data_connection, args=(conn, addr), daemon=True).start()

def main():
    print(f"[{ROLE.upper()}] Node aktif di port {PORT}")
    threading.Thread(target=data_listener, daemon=True).start()

    if is_primary:
        threading.Thread(target=heartbeat_sender, daemon=True).start()
    else:
        threading.Thread(target=heartbeat_listener, daemon=True).start()
        threading.Thread(target=heartbeat_monitor, daemon=True).start()

    while True:
        time.sleep(1)

if __name__ == "__main__":
    main()