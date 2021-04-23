from threading import Thread,currentThread, Lock, RLock, Semaphore
import requests
import os
import shutil

semaphore = Semaphore(0)
hasilperhitungan=0

class hanifCopy (Thread):
   def __init__(self,name,thread_number,namafile):
       Thread.__init__(self)    
       self.threadLock = Lock()
       self.name = name
       self.thread_number = thread_number
       self.namafile=os.path.join(os.path.dirname(__file__), namafile)
       self.semaphore = semaphore

   def run(self):
       print("\n"+str(self.thread_number)+". ---> " + self.name + "mulai")
       print('menjalankan semaphore acquire')
       self.threadLock.acquire()
       self.semaphore.acquire()
       print('membaca file : '+self.namafile)
       self.readfile()
       print('menyalin file : '+self.namafile)
       self.copyfile()
       self.threadLock.release()
       print("\n"+str(self.thread_number)+". ---> " + currentThread().getName() + "selesai")

   def readfile(self):
       f = open(self.namafile, "r")
       print("file : "+f.read())
      
   def copyfile(self):
       shutil.copy('.\Chapter02\provinsi.txt', '.\Chapter02')
    
class hanifDua113040087 (Thread):
   def __init__(self, name,thread_number,a,namafile):
       Thread.__init__(self)
       self.threadLock = Lock()
       self.semaphore = semaphore
       self.rlock = RLock()
       self.name = name
       self.namafile=os.path.join(os.path.dirname(__file__), namafile)
       self.thread_number = thread_number
       self.a=a
      
   def run(self):
       print("\n"+str(self.thread_number)+". ---> " + self.name + "jalan")
       self.threadLock.acquire()
       print("threadlock acquire utama")
       self.hitung()
       self.threadLock.release()
       print("\n"+str(self.thread_number)+". ---> " + currentThread().getName() + "selesai")
         
   def apitempat(self):
       with self.rlock:
           print('mengakses web service')
           apiurl='https://dev.farizdotid.com/api/daerahindonesia/kota?id_provinsi='
           eq=str(self.a)
           response = requests.get(apiurl+eq)
           html=response.json()
           hasil = html["nama"]
           print("Nama Kabupaten : "+str(hasil))
           self.createfile(hasil)       

   def hitung(self):
       with self.rlock:
            print('rlock hitung')
            self.apitempat()
       
   def createfile(self,isi):
       print('membuat file baru : '+ self.namafile)
       f = open(self.namafile, "x")
       f.write(str(isi))
       f.close()
       print('me-release semaphore')
       self.semaphore.release()
       print('semaphore selesai di release')
       



