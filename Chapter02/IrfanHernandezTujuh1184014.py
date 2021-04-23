from threading import Thread
import os
import requests
from queue import Queue

queue = Queue()
drink = []

apiurl='https://www.thecocktaildb.com/api/json/v1/1/search.php?s=margarita'
response = requests.get(apiurl)
html=response.json()


class IrfanPut(Thread):
    def __init__(self, name, thread_number, filename):
        Thread.__init__(self)
        self.name = name
        self.thread_number = thread_number
        self.filename = os.path.join(os.path.dirname(__file__), filename)

    def margaritaapi(self):
        string = "Drinks :"
        for i in range(len(html["drinks"])):
            hasil = html["drinks"][i]["strDrink"]
            angka = "\n"+str(i)+". "
            string = string+angka+hasil
            drink.append(hasil)
            queue.put(drink)
            print(str(i)+'. Margarita %s Appended from queue by %s' % (hasil, self.name))
        self.fileresult(string)
    
    def fileresult(self, isi):
        f = open(self.filename+".txt", "w")
        f.write(isi)
        f.close()            
    
    def readfile(self):
       read = queue.get()
       r = len(read)
       while r > 0:
           f = open(self.filename+".txt", "r")
           baca = f.readlines()
           print('\n'+str(r)+' Tulis Readed from queue by %s' % ( self.name))
           print(baca[r])
           f.close()
           r = r - 1
           queue.task_done()
        
    def run(self):
        print("Start Queue!")
        self.margaritaapi()
        self.readfile()
        print("Queue Finish!")





