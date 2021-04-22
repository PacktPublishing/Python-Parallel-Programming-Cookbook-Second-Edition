from threading import Thread
from queue import Queue
import os 
import requests

queue = Queue()
ayo = []
apiurl ='https://www.thecocktaildb.com/api/json/v1/1/list.php?a=list'
response = requests.get(apiurl)
html=response.json()

class ayomaju(Thread):
    def __init__(self, namathread, filename):
        Thread.__init__(self)
        self.filename = os.path.join(os.path.dirname(__file__), filename)
        self.namathread = namathread
        
    def mainapi(self):
        string = "minuman:"
        for i in range(len(html["drinks"])):
            sini = html["drinks"][i]["strAlcoholic"]
            nomor = "\n"+str(i)+". "
            string = string + nomor + sini
            ayo.append(sini)
            queue.put(ayo)
            print(str(i)+". %s yg di append" % (sini))
        self.createfile(string)
        self.mundur()
            
    def run(self):
        print("Kita mulai queunya")
        self.mainapi()
        print("queue selesai")
        
    def createfile(self, isi):
        f = open(self.filename, "w")
        f.write(str(isi))
        f.close()
    
    def read(self):
        x = open(self.filename, "r")
        print(x.read())
        x.close() 
        
    def mundur(self):
        ayomundur = queue.get()
        dur = len(ayomundur)
        while dur > 0:
            print("hasil pop")
            dur = dur -1
        self.read()
        queue.task_done()
    
    
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        