import socket

HOST = '127.0.0.1' # The server's hostname or IP address
PORT = 9000        # The port used by the server

def send_data(message):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((HOST, PORT))
            s.sendall(message.encode())
            print(f"Pesan '{message}' berhasil dikirim ke {HOST}:{PORT}")
        except ConnectionRefusedError:
            print(f"Koneksi ditolak. Pastikan primary_server.py berjalan di {HOST}:{PORT}")
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")

if __name__ == "__main__":
    while True:
        user_input = input("Masukkan pesan untuk dikirim (ketik 'exit' untuk keluar): ")
        if user_input.lower() == 'exit':
            break
        send_data(user_input)