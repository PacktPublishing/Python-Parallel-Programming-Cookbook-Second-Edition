import time
from random import randint
from threading import Thread,currentThread, Lock, RLock, Semaphore
import requests
import os

semaphore = Semaphore(0)

class rollySemaphoreDeleteFile (Thread):
   def __init__(self,name,thread_number,namafile):
       Thread.__init__(self)    
       self.name = name
       self.thread_number = thread_number
       self.namafile=namafile
       self.semaphore = semaphore

   def run(self):
       print("\n"+str(self.thread_number)+". ---> " + self.name + "jalan")
       print('mau menjalankan semaphore acquire untuk baca dan delete file')
       self.semaphore.acquire()
       print('melakukan baca file')
       self.readfile()
       print('melakukan delete file')
       self.deletefile()
       print("\n"+str(self.thread_number)+". ---> " + currentThread().getName() + "selesai")

   def readfile(self):
       f = open(self.namafile, "r")
       print("Isi Filenya : "+f.read())
      
   def deletefile(self):
       os.remove(self.namafile)
    
class rollyDua113040087 (Thread):
   def __init__(self, name,thread_number,a,b ,namafile):
       Thread.__init__(self)
       self.threadLock = Lock()
       self.semaphore = semaphore
       self.rlock = RLock()
       self.name = name
       self.namafile = namafile
       self.thread_number = thread_number
       self.a=a
       self.b=b
      
   def run(self):
       print("\n"+str(self.thread_number)+". ---> " + self.name + "jalan")
       self.threadLock.acquire()
       print("threeadlock acquire utama")
       self.hitung()
       self.threadLock.release()
       print("\n"+str(self.thread_number)+". ---> " + currentThread().getName() + "selesai")
         
   def apipangkat(self):
       with self.rlock:
           print('didalam rlock apipangkat, akses web service...')
           apiurl='https://api.mathjs.org/v4/?expr='
           eq=str(self.a)+'^'+str(self.b)
           response = requests.get(apiurl+eq)
           html=response.content.decode(response.encoding)
           hasil = int(html)
           print("hasil : "+str(hasil))
           self.createfile(hasil)

   def hitung(self):
       with self.rlock:
            print('rlock hitung')
            self.apipangkat()

   def deletefile(self):
       print('mau menjalankan semaphore acquire')
       self.semaphore.acquire()
       print('semaphore acquire')
       os.remove(self.namafile)
    
   def createfile(self,isi):
       self.semaphore.release()
       print('di dalam Semaphore release, membuat file baru')
       f = open(self.namafile, "x")
       f.write(str(isi))
       f.close()



