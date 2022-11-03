import threading
import requests
from queue import Queue
import os

event = threading.Event()
queue = Queue()

class HanifCopy (threading.Thread):
   def __init__(self, name, thread_number, filename):
       threading.Thread.__init__(self)  
       self.name = name
       self.threadLock = threading.Lock()
       self.thread_number = thread_number
       self.filename=os.path.join(os.path.dirname(__file__), filename)

   def run(self):
       print("\n"+str(self.thread_number)+". ---> " + self.name + "start.")
       self.threadLock.acquire()
       event.wait()
       print('Copy file : '+self.filename)
       self.readfile()
       print("Read file")
       self.copyfile()
       event.clear()
       self.threadLock.release()
       print("\n"+str(self.thread_number)+". ---> " + threading.currentThread().getName() + "end")

   def readfile(self):
       f = open(self.filename, "r")
       print("Isi file : "+f.read())
      
   def copyfile(self):
       queue.get()
       with open ("F:\\Kuliah\\Semester 6\\Sistem Tersebar\\Python-Parallel-Programming-Cookbook-Second-Edition\\Chapter02\\pokemon.txt", "rb") as read:
        with open ("F:\\Kuliah\\Semester 6\\Sistem Tersebar\\Python-Parallel-Programming-Cookbook-Second-Edition\\pokemon.txt", "wb") as filetobecopied:
            filetobecopied.write(read.read())
       queue.task_done()

       
class HanifTujuh1184058 (threading.Thread):
   def __init__(self, name, thread_number, a ,filename):
       threading.Thread.__init__(self)
       self.threadLock = threading.Lock()
       self.name = name
       self.rlock = threading.RLock()
       self.filename=os.path.join(os.path.dirname(__file__), filename)
       self.thread_number = thread_number
       self.a=a
      
   def run(self):
       print("\n"+str(self.thread_number)+". ---> " + self.name + "start.")
       self.count()
       event.set()
       print("\n"+str(self.thread_number)+". ---> " + threading.currentThread().getName() + "finish.")
         
   def getapi(self):
       with self.rlock:
           print('Akses web service')
           apiurl='https://pokeapi.co/api/v2/pokemon/ditto'
           response = requests.get(apiurl)
           html=response.json()
           string = "ability :"
           global x
           x = self.a
           for i in range(len(html["abilities"])):
               hasil = html["abilities"][i]["ability"]["name"]
               tulis = "\n"+str(i)+". "
               string = string+tulis+str(hasil)
               queue.put(x)
               print('%d Writed from queue by %s' % (x, self.name))
               x = x-1
           self.createfile(string)  

   def count(self):
       with self.rlock:
            self.getapi()
       
   def createfile(self,isi):
       print('Create File : '+ self.filename)
       f = open(self.filename, "w")
       f.write(str(isi))
       f.close()