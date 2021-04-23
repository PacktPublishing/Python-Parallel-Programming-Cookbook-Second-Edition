from threading import Thread
import os
import requests
from queue import Queue

drink = []
queue = Queue()

apiurl='https://www.thecocktaildb.com/api/json/v1/1/list.php?g=list'
response = requests.get(apiurl)
html=response.json()


class Anisa(Thread):
    def __init__(self, name, thread_number, filename):
        Thread.__init__(self)
        self.name = name
        self.thread_number = thread_number
        self.filename = os.path.join(os.path.dirname(__file__), filename)

    def Glassapi(self):
        string = "Drinks :"
        for i in range(len(html["drinks"])):
            hasil = html["drinks"][i]["strGlass"]
            angka = "\n"+str(i)+". "
            string = string+angka+hasil
            drink.append(hasil)
            queue.put(drink)
            print(str(i)+'. Jenis Glass %s Appended from queue by %s' % (hasil, self.name))
        self.fileresult(string)
    
    def fileresult(self, isi):
        f = open(self.filename+".txt", "w")
        f.write(isi)
        f.close()            
        read = queue.get()
        r = len(read)
        while r > 0:
           f = open(self.filename+".txt", "r")
           baca = f.readlines()
           print('\n'+str(r)+' Hasil Readed from queue by %s' % ( self.name))
           print(baca[r])
           f.close()
           r = r - 1
           queue.task_done()
        
    def run(self):
        print("Mulai Queue!")
        self.Glassapi()
        print("Queue Selesai!")
