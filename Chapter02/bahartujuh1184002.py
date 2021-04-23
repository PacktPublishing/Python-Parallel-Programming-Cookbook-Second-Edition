import threading
import requests
import os
from queue import Queue 

queue = Queue()
event = threading.Event()

class BaharQue(threading.Thread):
   def __init__(self,name, filename):
       threading.Thread.__init__(self)  
       self.name = name
       self.threadLock = threading.Lock()
       self.filename = os.path.join(os.path.dirname(__file__), filename)

   def run(self):
       print("\n"+ self.name + "mulai.")
       self.threadLock.acquire()
       print('kodepos')
       event.wait()
       print('ubah : '+self.filename)
       self.baca()
       print("kode sudah diubah")
       self.buat()
       event.clear()
       self.threadLock.release()
       print("\n" + threading.currentThread().getName() + "berhasil")

   def baca(self):
       f = open(self.filename, "r")
       print("isi file : \n "+f.read())
      
   def buat(self):
       f = open(self.filename, "r")
       bikin = open(self.filename+'.txt', "w")
       for line in f:
           bikin.write(line.replace('kodepos', 'kelurahan'))
       bikin.close()
       new = open(self.filename+'.txt', "r")
       print(new.read())
       new.close()

       
class Bahartujuh1184002 (threading.Thread):
   def __init__(self, name, filename):
       threading.Thread.__init__(self)
       self.threadLock = threading.Lock()
       self.name = name
       self.rlock = threading.RLock()
       self.filename=os.path.join(os.path.dirname(__file__), filename)


   def run(self):
       print("\n"+ self.name + " mulai.")
       self.main()
       cb = queue.get()
       print("\n queuenya")
       print(cb)
       queue.task_done()
       event.set()
       print("\n" + threading.currentThread().getName() + "selesai.")
         
   def webapi(self):
       with self.rlock:
           print('Webservice nya')
           apiurl='https://nbc.vanmason.web.id/service/kodepos/42173'
           response = requests.get(apiurl)
           html=response.json()
           string = ""
           for i in range(len(html["kodepos"])):
               baru = html["kodepos"][i]["kelurahan"]
               new = "\n"+str(i)+". "
               string = string+new+str(baru)
           queue.put(string)
           self.createfile(string)
           

   def main(self):
       with self.rlock:
            self.webapi()
       
   def createfile(self,isi):
       print('Create File : '+ self.filename)
       f = open(self.filename, "w")
       f.write(str(isi))
       f.close()
       
       
       
