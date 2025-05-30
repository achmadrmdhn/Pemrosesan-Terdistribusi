import socket
import threading

BACKUPS = [("127.0.0.1", 9001), ("127.0.0.1", 9002)]
PRIMARY_PORT = 9000

def send_to_backups(data):
    for ip, port in BACKUPS:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((ip, port))
                s.sendall(data.encode())
        except Exception as e:
            print(f"Gagal mengirim ke backup {ip}: {port} {e}")

def handle_client(conn, addr):
    print(f" [PRIMARY] Koneksi dari {addr}")
    while True:
        try:
            data = conn.recv(1024).decode()
            if not data:
                break
            print(f"[PRIMARY] Menerima data: {data}")
            send_to_backups(data)
        except:
            break
    conn.close()
    print(f"[PRIMARY] Koneksi dengan {addr} ditutup")

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('127.0.0.1', PRIMARY_PORT))
        s.listen()
        print(f" [PRIMARY] Server berjalan di port {PRIMARY_PORT}")
        while True:
            conn, addr = s.accept()
            threading.Thread(target=handle_client, args=(conn, addr)).start()

if __name__ == "__main__":
    main()