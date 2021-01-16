import threading,random


class prod_cons_thread(threading.Thread):
    


    def __init__(self,Thread_id) -> None:
        threading.Thread.__init__(self)
        self.Thread_id = Thread_id
        
    #producer
    def run_prod(self,val):

        spazio_disp.acquire()
        
        global buff
        buff = val
        print("prodotto")

        messa_disp.release()
    #consumer
    def run_cons(self):

        messa_disp.acquire()
        global buff
        ret =  buff
        print("consumato",ret)
   
        spazio_disp.release()



#init semaphore
spazio_disp = threading.Semaphore(1)
messa_disp = threading.Semaphore(0)

#init buff
buff = None

#init thread
prod = prod_cons_thread(1)
cons = prod_cons_thread(2)


prod.run_prod(random.randint(1,25))


cons.run_cons()



