from threading import Thread
from queue import Queue
import os 
import requests

queue = Queue()
lagi = []
apiurl ='https://www.thecocktaildb.com/api/json/v1/1/list.php?i=list'
response = requests.get(apiurl)
html=response.json()

class vickysaf(Thread):
    def __init__(self, namathread, filename):
        Thread.__init__(self)
        self.filename = os.path.join(os.path.dirname(__file__), filename)
        self.namathread = namathread

    def mainapi(self):
        string = "nama kota:"
        for i in range(len(html["drinks"])):
            sini = html["drinks"][i]["strIngredient1"]
            nomor = "\n"+str(i)+". "
            string = string + nomor + sini
            lagi.append(sini)
            queue.put(lagi)
            print(str(i)+". %s yg di append" % (sini))
        self.createfile(string)
        self.belakang()

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