from threading import Thread,currentThread, Lock, RLock, Event
import requests
import os
from queue import Queue 

queue = Queue()
event = Event()

class raviMenulis (Thread):
   def __init__(self,name,thread_number,namafile):
       Thread.__init__(self)    
       self.threadLock = Lock()
       self.name = name
       self.thread_number = thread_number
       self.namafile=os.path.join(os.path.dirname(__file__), namafile)
       self.event = event

   def run(self):
        print("\n"+str(self.thread_number)+". ---> " + self.name + "GO!!")
        print('class raviMenulis mau menjalankan event wait, setelah itu clear untuk baca dan rename file')
        self.event.wait()
        self.threadLock.acquire()
        print('Action read file : '+self.namafile)
        self.readfile()
        print('Action rename file : '+self.namafile)
        self.unamofile()
        self.event.wait()
        self.threadLock.release()
        print("\n"+str(self.thread_number)+". ---> " + currentThread().getName() + "Baca dan delete file done")
        print ("menjalankan event clear")
        self.event.clear()

   def readfile(self):
       q=queue.get()
       f = open(self.namafile, "r")
       print("Isi Filenya: "+f.read())
       print("Done!!, jalanin queue task done \n")
       queue.task_done()
      
   def unamofile(self):
       print('Ganti Nama File \n')
       os.rename(self.namafile,self.namafile+'.txt')
       print("nama file diganti ya \n")
    
class raviTujuh1184040 (Thread):
   def __init__(self, name,thread_number,r,f ,namafile):
       Thread.__init__(self)
       self.threadLock = Lock()
       self.event = event
       self.rlock = RLock()
       self.name = name
       self.namafile=os.path.join(os.path.dirname(__file__), namafile)
       self.thread_number = thread_number
       self.r=r
       self.f=f
      
   def run(self):
       print("\n"+str(self.thread_number)+". ---> " + self.name + "GO!!")
       self.threadLock.acquire()
       print("threeadlock acquire utama")
       self.hitung()
       self.event.set()
       print('class raviTujuh1184068 selesai untuk event set')
       self.threadLock.release()
       print("\n"+str(self.thread_number)+". ---> " + currentThread().getName() + "selesai")
         
   def Aapi(self):
       with self.rlock:     
           print('didalam rlock apipangkat, akses web service...')
           apiurl='http://www.emsifa.com/api-wilayah-indonesia/api/regencies/13.json'
           response = requests.get(apiurl)
           html=response.json()
           queue.put(html)
           self.createfile(html)     

   def hitung(self):
       with self.rlock:
            print('rlock hitung')
            self.Aapi()
       
   def createfile(self,isi):
       print('Buat file baru : '+ self.namafile)
       f = open(self.namafile, "x")
       f.write(str(isi))
       f.close()
       print('file baru sudah dibuat, mau menjalankan event set')
       
