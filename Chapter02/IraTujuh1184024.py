from threading import Thread,currentThread, Lock, RLock, Event
import requests
import os
from queue import Queue 

queue = Queue()
event = Event()

class iraHandlingFile (Thread):
   def __init__(self,name,thread_number,namafile):
       Thread.__init__(self)    
       self.threadLock = Lock()
       self.name = name
       self.thread_number = thread_number
       self.namafile=os.path.join(os.path.dirname(__file__), namafile)
       self.event = event

   def run(self):
        print("\n"+str(self.thread_number)+". ---> " + self.name + "jalan")
        print('class iraHandlingFile menjalankan event wait dilanjutkan clear untuk baca dan rename file')
        self.event.wait()
        self.threadLock.acquire()
        print('melakukan baca file : '+self.namafile)
        self.readfile()
        print('melakukan rename file : '+self.namafile)
        self.renamefile()
        self.event.wait()
        self.threadLock.release()
        print("\n"+str(self.thread_number)+". ---> " + currentThread().getName() + "Baca file dan delete file sudah selesai")
        print ("menjalankan event clear")
        self.event.clear()

   def readfile(self):
       q=queue.get()
       f = open(self.namafile, "r")
       print("melihat apa isi file : "+f.read())
       print("selesai membaca isi file , jalanin queue task done \n")

       a = open(self.namafile, "a+")
       a.write("\n ini adalah api tentang menampilkan gambar kucing %d\r\n")
       a.close()
       print('Setelah append file')
       queue.task_done()
      
   def renamefile(self):
       print('mengganti nama file \n')
       os.rename(self.namafile,self.namafile+'.txt')
       print("nama file telah diganti \n")
    
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
            print('rlock hitung')
            self.getapi()
       
   def createfile(self,isi):
       print('membuat file baru : '+ self.namafile)
       f = open(self.namafile, "x")
       f.write(str(isi))
       f.close()
       print('sudah selesai membuat file baru, mau menjalankan event set')
       
