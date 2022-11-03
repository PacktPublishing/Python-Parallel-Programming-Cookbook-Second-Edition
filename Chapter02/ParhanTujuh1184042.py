from threading import Thread,currentThread, Lock, RLock, Event
import requests
import os
from queue import Queue 

queue = Queue()
event = Event()

class parhanmanajemenFile (Thread):
   def __init__(self,name,thread_number,namafile):
       Thread.__init__(self)    
       self.threadLock = Lock()
       self.name = name
       self.thread_number = thread_number
       self.namafile=os.path.join(os.path.dirname(__file__), namafile)
       self.event = event

   def run(self):
        print("\n"+str(self.thread_number)+". ---> " + self.name + "jalan")
        print('pada class parhanmanajemenFile jalankan event wait lalu clear untuk read dan rename file')
        self.event.wait()
        self.threadLock.acquire()
        print('membaca file : '+self.namafile)
        self.readfile()
        print('merename file : '+self.namafile)
        self.event.wait()
        self.renamefile()
        self.threadLock.release()
        print("\n"+str(self.thread_number)+". ---> " + currentThread().getName() + "Baca file dan delete file selesai")
        print ("jalankan event clear")
        self.event.clear()

   def readfile(self):
       q=queue.get()
       f = open(self.namafile, "r")
       print("isi file yang di read : "+f.read())
       print("setelah baca file, jalankan queue task done \n")
       queue.task_done()
      
   def renamefile(self):
       print('ganti nama file \n')
       os.rename(self.namafile,self.namafile+'.txt')
       print("nama file telah diganti \n")
       
class parhanTujuh1184042 (Thread):
   def __init__(self, name,thread_number,a,b ,namafile):
       Thread.__init__(self)
       self.threadLock = Lock()
       self.event = event
       self.rlock = RLock()
       self.name = name
       self.namafile=os.path.join(os.path.dirname(__file__), namafile)
       self.thread_number = thread_number
       self.a=a
       self.b=b
      
   def run(self):
       print("\n"+str(self.thread_number)+". ---> " + self.name + "jalan")
       self.threadLock.acquire()
       print("threeadlock acquire utama")
       self.jumlah()
       self.event.set()
       print('class parhanTujuh1184042 selesai melakukan event set')
       self.threadLock.release()
       print("\n"+str(self.thread_number)+". ---> " + currentThread().getName() + "selesai")
         
   def apiservice(self):
       with self.rlock:     
           print('didalam rlock apiservice, akses web service...')
           apiurl='https://gempa-api-zhirrr.vercel.app/api/gempa'
           response = requests.get(apiurl)
           z=response.json()
           queue.put(z)
           self.createfile(z)     

   def jumlah(self):
       with self.rlock:
            print('rlock jumlah')
            self.apiservice()
       
   def createfile(self,isi):
       print('buat file baru : '+ self.namafile)
       f = open(self.namafile, "x")
       f.write(str(isi))
       f.close()
       print('sudah buat file baru, jalankan event set')
       
