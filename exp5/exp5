import time
from multiprocessing import Process,Lock,Value

def add_500_no_lock(total):
    for i in range(100):
        time.sleep(0.01)
        total.value += 5

def sub_500_no_lock(total):
    for i in range(100):
        time.sleep(0.01)
        total.value -= 5
        

if _name_ == '_main_':
    
    total = Value('i',500)
    
    add_process = Process(target=add_500_no_lock, args=(total,))
    sub_process = Process(target=sub_500_no_lock, args=(total,))
    
    add_process.start()
    sub_process.start()
    
    add_process.join()
    sub_process.join()
    
    print(total.value)