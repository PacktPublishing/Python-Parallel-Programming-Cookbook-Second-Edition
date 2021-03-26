from threading import Thread, currentThread, Lock, RLock, Semaphore
import requests
import os

class josua1184091Arrangement (Thread):

   def __init__(self, nama, thread_number, filenya):
       Thread.__init__(self)
       self.threadLock = Lock()
       self.nama = nama
       self.thread_number = thread_number
       self.filenya=os.path.join(os.path.dirname(__file__), filenya)
       self.semaphore = semaphore

   def jalankan(self):
       print("\n"+str(self.thread_number)+". ---> " + self.nama + "run")
       print('run semaphore yaitu untuk membuat dan menghapus file')
       self.threadLock.acquire()
       self.semaphore.acquire()
       
       print('buat file : '+self.filenya)
       self.createfile()
       
       print('hapus file : '+self.filenya)
       self.deletefile()
       self.threadLock.release()
       #print("\n"+str(self.thread_number)+". ---> " + currentThread().getName() + "selesai")

    def bacafile(self):
       f = open(self.filenya, "r")
       print("Josua1184091 : "+f.read())
      
    def ubahnamafile(self):
       os.rename(self.filenya,self.filenya+'.Josuainthehouse')
       
  class josua1184091Api (Thread):
   def __init__(self, nama,thread_number,filenya, bravo, delta):
       Thread.__init__(self)
       self.threadLock = Lock()
       self.semaphore = semaphore
       self.rlock = RLock()
       self.nama = nama
       self.filenya=os.path.join(os.path.dirname(__file__), filenya)
       self.thread_number = thread_number
       self.bravo=bravo
       self.delta=delta
      
   def jalankan(self):
       print("\n"+str(self.thread_number)+". ---> " + self.nama + "run")
       self.threadLock.acquire()
       
       print("ini adalah threadlock aqcuire")     
       self.kalkulasi()
       
       self.threadLock.release()
       
       print("\n"+str(self.thread_number)+". ---> " + currentThread().getName() + "yoi beres")
       
       
       
   def fungsiapi(self):
       with self.rlock:
           
           api_url='https://api.twitter.com/1.1/followers/list.json'
           
           print('Mengakses fungsi api web service dari twitter untuk mengambil view list follower yang ada pada username twitter saya josh0018 pada Rlock')
           
           eq=str(self.bravo)+'^'+str(self.delta)
           response = requests.get(api_url+eq)
           html=response.content.decode(response.encoding)
           hasil = int(html)
           print("result : "+str(result))
           self.createfile(result)       

   def kalkulasi(self):
       with self.rlock:
            self.fungsiapi()
            print('mengkalkulasi Rlock')
       
   def buatfile(self,konten):
       print('buat file : '+ self.filenya)
       f = open(self.filenya, "x")
       f.write(str(konten))
       f.close()
       print('buat file baru')
       self.semaphore.release()
       print('semaphore sudah di release')
       



