import threading
import time
from datetime import datetime

def task1():
    print("Task 1: Membaca file")
    time.sleep(5)
def task2():
    print("Task 2: Memproses data")
    time.sleep(5)
def task3():
    print("Task 3: Menyimpan data")
    time.sleep(5)
awal = datetime.today()
print(awal)
task1()
task2()
task3()
akhir = datetime.today()
print(akhir)


"""
# Membuat dua thread untuk menjalankan task1 dan task2 secara bersamaan
t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)
t3 = threading.Thread(target=task3)
awal = datetime.today()
print(awal)
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
akhir = datetime.today()
print(akhir)
"""
