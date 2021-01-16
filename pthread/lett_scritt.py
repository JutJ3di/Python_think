import builtins
import threading,random
import time
from typing import NoReturn

class lett(threading.Thread):
    
    

    def __init__(self,Number_thread):
        threading.Thread.__init__(self)
    
    def run(self):
        for n in range(10):
            mutex.acquire()
            global num_lett 
            num_lett  += 1
            if num_lett == 1:
                sync.acquire()
            mutex.release()
            global buff 
            print("valore letto",buff)
            time.sleep(2)
            mutex.acquire()
            num_lett -= 1
            if num_lett== 0:
                sync.release()
            mutex.release()


class scritt(threading.Thread):

    def __init__(self,Number_thread):
        threading.Thread.__init__(self)
    def run(self) -> None:
        for n in range(10):
            sync.acquire()
            global buff 
            buff = random.randint(12,453)
            sync.release()



sync = threading.Semaphore(1)
mutex = threading.Lock()

num_lett = 0
buff = None

threads = []

thread_scritt = scritt(1)

thread_scritt.start()

thread_scritt_2 = scritt(4)

thread_scritt_2.start()

thread_scritt_3 = scritt(5)

thread_scritt_3.start()



thread_lett_1 = lett(2)


thread_lett_1.start()

thread_lett_2 = lett(3)

thread_lett_2.start()

threads.append(thread_lett_1)
threads.append(thread_lett_2)
threads.append(thread_scritt_2)
threads.append(thread_scritt_3)
threads.append(thread_scritt)


for t in threads:
    t.join()
