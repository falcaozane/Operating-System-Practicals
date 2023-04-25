import threading
import queue as queue
import time

queue = queue.Queue(5)

def pro():
    global queue
    while True:
        if not queue.full():
            item = time.time()
            queue.put(item)
            print("Produced item: ",item)
            time.sleep(1)
            
def cons():
    global queue
    while True:
        if not queue.empty():
            item = queue.get()
            print("Consumed item: ",item)
        time.sleep(2)
        
producer_thread = threading.Thread(target=pro)
consumer_thread = threading.Thread(target=cons)

producer_thread.start()
consumer_thread.start()
producer_thread.join()
consumer_thread.join()