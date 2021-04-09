# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 13:56:38 2021

@author: ASUS
"""

import logging
import threading
import time

LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

items = []
condition = threading.Condition()


class josua1184091Write_Trier(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
     

    def trying(self):

        with condition:
            f = open("josh123.txt", "w+")
            for i in range(10):
                f.write("hi are you okay number %d\r\n" % (i+1))
            
            if len(items) == 0:
                logging.info('no items to try')
                
                condition.wait()

            items.pop()
            logging.info('tried 1 item')

            condition.notify()

            
    def run(self):
        for i in range(20):
            time.sleep(2)
            self.trying()


class josua1184091_Catcher(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def apiJosua(self):
            print('Dalam apiJosua, akses webservice...')
            apiurl='https://www.beanstream.com/api/v1'
            eq=str(self.r)+'*'+str(self.f)
            requests=str()
            response = requests.get(apiurl)
            html=response.content.decode(response.encoding)
            hasil = int(html)
            string = "hasil isinya = "
            i = 1
            for i in range (1,10):
                konten = (1,10)
                items.append(konten)
                string = string+str(i)
                i = i + 1
                self.createfile(string)
                x = open(self.nfile, "r+")
                print(x.read())
                konten = (1,10)
                items.append(konten)

    def catching(self):

        with condition:

            if len(items) == 10:
                logging.info('items cathed {}. Stopped'.format(len(items)))
                condition.wait()

            items.append(1)
            logging.info('total items {}'.format(len(items)))

            condition.notify()

    def run(self):
        for i in range(20):
            time.sleep(1)
            self.catching()


def main():
    josh_catcher = josua1184091_Catcher(name='Josh_Catcher')
    josh_trier = josua1184091Write_Trier(name='Josh_Trier')

    josh_catcher.start()
    josh_trier.start()

    josh_catcher.join()
    josh_trier.join()


if __name__ == "__main__":
    main()
