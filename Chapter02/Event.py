import logging
import threading
import time
import random

#LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
#logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

items = []
event = threading.Event()


class Consumer(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def run(self):
        a=0
        while True:
        #for i in range(5):
            time.sleep(2)
            print('Konsumer : menunggu event set dari produser, status event.wait')
            event.wait() #menunggu jika event=False / jika event=true maka event jalan
            isinya=items.pop()
            print(str(a)+'. Konsumer : sudah di pop,tumpukan list sebanyak : '+str(len(items))+' isinya : '+str(isinya))
            #logging.info('Consumer notify: {} popped by {}'.format(item, self.name))
            a=a+1
            print('Konsumer : event clear')
            event.clear() # set event=false

class Producer(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def run(self):
        for i in range(5):#ini perulangan berapa kali
            time.sleep(2)
            isinya = random.randint(0, 100)
            items.append(isinya) # add items
            print(str(i)+'. Produser : sudah di append,tumpukan list sebanyak : '+str(len(items))+' isinya : '+str(isinya))
            #logging.info('Producer notify: item {} appended by {}'.format(item, self.name))
            print('Produser : event set')
            event.set() # karena dia cuma ngubah variabel jadi true, jika set dan clear jalan cepat beberapa kali, itu dianggap satu kali jika ketemu wait

if __name__ == "__main__":
    t1 = Producer()
    t2 = Consumer()

    t2.start()
    t1.start()

    #t1.join()
    #t2.join()
