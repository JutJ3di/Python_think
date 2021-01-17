import queue,threading,time,random

q = queue.SimpleQueue()#queue.Queue

def consumer():
    for n in range(10):
        val = q.get()
        print("valore preso dalla queue val",val)
        #q.task_done()        



def producer():
    for n in range(10):
        x = random.randint(1,100)
        q.put(item=x)
        print("Produzione")
        time.sleep(1)    





threading.Thread(target=consumer).start()
threading.Thread(target=producer).start()


#q.join()

