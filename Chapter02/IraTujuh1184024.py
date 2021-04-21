from threading import Thread,currentThread, Lock, RLock, Event
import requests
import os
from queue import Queue 

queue = Queue()
event = Event()

class iraRemoveFile (Thread):
   def __init__(self,name,thread_number,namafile):
       Thread.__init__(self)    
       self.threadLock = Lock()
       self.name = name
       self.thread_number = thread_number
       self.namafile=os.path.join(os.path.dirname(__file__), namafile)
       self.event = event

   def run(self):
        print("\n"+str(self.thread_number)+". ---> " + self.name + "jalan")
        print('class iraRemoveFile ingin menjalankan event')
        self.event.wait()
        self.threadLock.acquire()
        print('membaca file : '+self.namafile)
        self.readfile()
        print('rename file : '+self.namafile)
        self.renamefile()
        self.event.wait()
        self.threadLock.release()
        print("\n"+str(self.thread_number)+". ---> " + currentThread().getName() + "membaca file dan menghapus file telah selesai")
        print ("menjalankan event selesai")
        self.event.clear()

   def readfile(self):
       q=queue.get()
       f = open(self.namafile, "r")
       print("isi file  : "+f.read())
       print("Selesai membaca file, jalanin queue task done \n")
       queue.task_done()
      
   def renamefile(self):
       print('mengganti nama file \n')
       os.rename(self.namafile,self.namafile+'.txt')
       print("nama file sudah diganti \n")

   def removefile(self):
       print('menghapus atau meremove file  \n')
       os.remove(self.namafile+'.txt')
       print("file sudah diremove \n")
    
class iraTujuh1184024 (Thread):
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
       self.hitung()
       self.event.set()
       print('class iraTujuh1184024 sudah selesai melakukan event set')
       self.threadLock.release()
       print("\n"+str(self.thread_number)+". ---> " + currentThread().getName() + "selesai")
         
   def getapi(self):
       with self.rlock:     
           print('akses web service...')
           apiurl='https://api.thecatapi.com/v1/images/search'
           response = requests.get(apiurl)
           html=response.json()
           queue.put(html)
           self.createfile(html)     

   def hitung(self):
       with self.rlock:
            self.getapi()
       
   def createfile(self,isi):
       print('membuat file baru : '+ self.namafile)
       f = open(self.namafile, "x")
       f.write(str(isi))
       f.close()
       print('sudah membuat file baru, mau menjalankan event set')
       
