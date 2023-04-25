import time
from multiprocessing import Process,Lock,Value

def add_500_lock(total,lock):
    for i in range(100):
        time.sleep(0.005)
        lock.acquire()
        total.value += 5
        lock.release()

def sub_500_lock(total,lock):
    for i in range(100):
        time.sleep(0.005)
        lock.acquire()
        total.value -= 5
        lock.release()
        

if __name__ == '__main__':
    
    total = Value('i',500)
    lock=Lock()
    add_process = Process(target=add_500_lock, args=(total,lock))
    sub_process = Process(target=sub_500_lock, args=(total,lock))
    add_process.start()
    sub_process.start()
    add_process.join()
    sub_process.join()
    print(total.value)