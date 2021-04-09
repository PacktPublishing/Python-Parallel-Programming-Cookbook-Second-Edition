import threading
import requests
import os

event = threading.Event()

class FerdyEventGI(threading.Thread):
   def __init__(self,name, thread_number, filename):
       threading.Thread.__init__(self)  
       self.name = name
       self.threadLock = threading.Lock()
       self.thread_number = thread_number
       self.filename = os.path.join(os.path.dirname(__file__), filename)

   def run(self):
       print("\n"+str(self.thread_number)+". ---> " + self.name + "mulai.")
       self.threadLock.acquire()
       print('Cocktail 1(')
       event.wait()
       print('ubah : '+self.filename)
       self.readfile()
       print("pas udah diubah")
       self.bikinfile()
       event.clear()
       self.threadLock.release()
       print("\n"+str(self.thread_number)+". ---> " + threading.currentThread().getName() + "berhasil")

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

       
class FerdyGITiga1184112 (threading.Thread):
   def __init__(self, name, thread_number ,filename):
       threading.Thread.__init__(self)
       self.threadLock = threading.Lock()
       self.name = name
       self.rlock = threading.RLock()
       self.filename=os.path.join(os.path.dirname(__file__), filename)
       self.thread_number = thread_number

      
   def run(self):
       print("\n"+str(self.thread_number)+". ---> " + self.name + "mulai.")
       self.hasil()
       print("Event")
       event.set()
       print("\n"+str(self.thread_number)+". ---> " + threading.currentThread().getName() + "selesai.")
         
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
           self.createfile(string)  
           x = open(self.filename, "r")
           print(x.read())

   def hasil(self):
       with self.rlock:
            self.apiwebservice()
       
   def createfile(self,isi):
       print('Create File : '+ self.filename)
       f = open(self.filename, "w")
       f.write(str(isi))
       f.close()
       
       
       

