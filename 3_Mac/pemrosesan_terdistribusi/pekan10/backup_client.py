import socket
import sys

def start_backup(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('127.0.0.1', port))
        s.listen()
        print(f" [BACKUP] Backup aktif di port {port}")
        while True:
            conn, addr = s.accept()
            with conn:
                data = conn.recv(1024).decode()
                if data:
                    print(f" [BACKUP: {port}] Replikasi data: {data}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python backup_client.py <PORT>")
    else:
        start_backup(int(sys.argv[1]))