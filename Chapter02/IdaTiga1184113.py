import logging
import threading
import time

LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

items = []
condition = threading.Condition()


class ida1184113_Catcher (threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
     

    def trying(self):

        with condition:
            f = open("idanilai.txt", "w+")
            for i in range(10):
                f.write("how are you? %d\r\n" % (i+1))
            
            if len(items) == 0:
                logging.info('no items to consume')
                
                condition.wait()

            items.pop()
            logging.info('consumed 1 item')

            condition.notify()

            
    def run(self):
        for i in range(20):
            time.sleep(2)
            self.trying()


class ida1184113Write_Trier(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def apiIda(self):
            print('Dalam apiIda, akses webservice...')
            apiurl='https://api.instagram.com/v1/tags/{tag-name}/media/recent'
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
            time.sleep(0.5)
            self.catching()
            