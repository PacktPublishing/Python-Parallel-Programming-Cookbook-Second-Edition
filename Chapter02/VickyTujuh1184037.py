from threading import Thread
from queue import Queue
import os 
import requests

queue = Queue()
lagi = []
apiurl ='https://data.covid19.go.id/public/api/prov.json'
response = requests.get(apiurl)
html=response.json()

class vickysaf(Thread):
    def __init__(self, namathread, filename):
        Thread.__init__(self)
        self.filename = os.path.join(os.path.dirname(__file__), filename)
        self.namathread = namathread

    def mainapi(self):
        string = "kertas:"
        for i in range(len(html["pena"])):
            sini = html["pena"][i]["strBuku"]
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