from threading import Thread
from queue import Queue
import os 
import requests

queue = Queue()
coba = []
apiurl ='https://kodepos-2d475.firebaseio.com/list_kotakab/p9.json?print=pretty'
response = requests.get(apiurl)
html=response.json()

class vickysaf(Thread):
    def __init__(self, namathread, filename):
        Thread.__init__(self)
        self.filename = os.path.join(os.path.dirname(__file__), filename)
        self.namathread = namathread
        
    def mainapi(self):
        string = "kertas:"
        for i in range(len(html["paper"])):
            sini = html["paper"][i]["buku"]
            nomor = "\n"+str(i)+". "
            string = string + nomor + sini
            coba.append(sini)
            queue.put(coba)
            print(str(i)+". %s yg di append" % (sini))
        self.createfile(string)
        self.kebelakang()
            
    def run(self):
        print("Dimulai")
        self.mainapi()
        print("Selesai")
        
    def createfile(self, isi):
        f = open(self.filename, "w")
        f.write(str(isi))
        f.close()
    
    def read(self):
        x = open(self.filename, "r")
        print(x.read())
        x.close() 
        
    def belakang(self):
        kebelakang = queue.get()
        dur = len(kebelakang)
        while dur > 0:
            print("hasil pop")
            dur = dur -1
        self.read()
        queue.task_done()
    
    
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        