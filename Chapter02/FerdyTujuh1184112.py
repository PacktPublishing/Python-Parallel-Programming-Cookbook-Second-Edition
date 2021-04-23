import threading
import requests
import os
from queue import Queue 

queue = Queue()
event = threading.Event()

class FerdyQueue(threading.Thread):
   def __init__(self,name, filename):
       threading.Thread.__init__(self)  
       self.name = name
       self.threadLock = threading.Lock()
       self.filename = os.path.join(os.path.dirname(__file__), filename)

   def run(self):
       print("\n"+ self.name + "mulai.")
       self.threadLock.acquire()
       print('Cocktail 1')
       event.wait()
       print('ubah : '+self.filename)
       self.readfile()
       print("pas udah diubah")
       self.bikinfile()
       event.clear()
       self.threadLock.release()
       print("\n" + threading.currentThread().getName() + "berhasil")

   def readfile(self):
       f = open(self.filename, "r")
       print("File's Content is : \n "+f.read())
      
   def bikinfile(self):
       f = open(self.filename, "r")
       bikin = open(self.filename+'.txt', "w")
       for line in f:
           bikin.write(line.replace('strCategory', 'Jenis'))
       bikin.close()
       baru = open(self.filename+'.txt', "r")
       print(baru.read())
       baru.close()

       
class Ferdy (threading.Thread):
   def __init__(self, name, filename):
       threading.Thread.__init__(self)
       self.threadLock = threading.Lock()
       self.name = name
       self.rlock = threading.RLock()
       self.filename=os.path.join(os.path.dirname(__file__), filename)


   def run(self):
       print("\n"+ self.name + "mulai.")
       self.hasil()
       cb = queue.get()
       print("\n queuenya")
       print(cb)
       queue.task_done()
       event.set()
       print("\n" + threading.currentThread().getName() + "selesai.")
         
   def apiwebservice(self):
       with self.rlock:
           print('Webservice nya')
           apiurl='https://www.thecocktaildb.com/api/json/v1/1/list.php?c=list'
           response = requests.get(apiurl)
           html=response.json()
           string = ""
           for i in range(len(html["drinks"])):
               cocokin = html["drinks"][i]
               baru = "\n"+str(i)+". "
               string = string+baru+str(cocokin)
           queue.put(string)
           self.createfile(string)  
           

   def hasil(self):
       with self.rlock:
            self.apiwebservice()
       
   def createfile(self,isi):
       print('Create File : '+ self.filename)
       f = open(self.filename, "w")
       f.write(str(isi))
       f.close()
       
       
       

