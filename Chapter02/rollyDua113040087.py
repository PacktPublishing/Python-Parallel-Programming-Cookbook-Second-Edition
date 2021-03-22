from threading import Thread,currentThread, Lock, RLock, Semaphore
import requests
import os

semaphore = Semaphore(0)
hasilperhitungan=0

class rollySemaphoreDeleteFile (Thread):
   def __init__(self,name,thread_number,namafile):
       Thread.__init__(self)    
       self.threadLock = Lock()
       self.name = name
       self.thread_number = thread_number
       self.namafile=os.path.join(os.path.dirname(__file__), namafile)
       self.semaphore = semaphore

   def run(self):
       print("\n"+str(self.thread_number)+". ---> " + self.name + "jalan")
       print('mau menjalankan semaphore acquire untuk baca dan delete file')
       self.threadLock.acquire()
       self.semaphore.acquire()
       print('melakukan baca file : '+self.namafile)
       self.readfile()
       print('melakukan rename file : '+self.namafile)
       self.renamefile()
       self.threadLock.release()
       print("\n"+str(self.thread_number)+". ---> " + currentThread().getName() + "selesai")

   def readfile(self):
       f = open(self.namafile, "r")
       print("Isi Filenya : "+f.read())
      
   def renamefile(self):
       os.rename(self.namafile,self.namafile+'.croot')
    
class rollyDua113040087 (Thread):
   def __init__(self, name,thread_number,a,b ,namafile):
       Thread.__init__(self)
       self.threadLock = Lock()
       self.semaphore = semaphore
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
       
   def createfile(self,isi):
       print('membuat file baru : '+ self.namafile)
       f = open(self.namafile, "x")
       f.write(str(isi))
       f.close()
       print('sudah membuat file baru, mau relese semaphore')
       self.semaphore.release()
       print('di dalam Semaphore release, semaphore sudah di release')
       



