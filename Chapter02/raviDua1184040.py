from threading import Thread,currentThread, Lock, RLock, Semaphore
import requests
import os

semaphore = Semaphore(0)
hasilperhitungan=0

class raviSemaphorewriteFile (Thread):
   def __init__(self,name,threadId,nfile):
       Thread.__init__(self)    
       self.threadLock = Lock()
       self.name = name
       self.threadId = threadId
       self.nfile=os.path.join(os.path.dirname(__file__), nfile)
       self.semaphore = semaphore

   def run(self):
       print("\n"+str(self.threadId)+". ---> " + self.name + "Mulai ya!")
       print('mau menjalankan semaphore acquire untuk baca dan tulis, buat ulang file')
       self.threadLock.acquire()
       self.semaphore.acquire()
       print('baca file dong : '+self.nfile)
       self.readfile()
       print('Tulis dan buat ulang file dong : '+self.nfile)
       self.writefile()
       self.threadLock.release()
       print("\n"+str(self.threadId)+". ---> " + currentThread().getName() + "Finish")

   def readfile(self):
       f = open(self.nfile, "r+")
       ##f.read(20) #Metode read(n) berfungsi untuk membaca sebanyak n karakter.
       print("Tampilin angkanya dong biar kita tau : \n "+f.read())
      
   def writefile(self):
       f = open(self.nfile, "r+")
       fc = open(self.nfile+'.html', "w")
       for line in f:
           fc.write(line.replace('Angka', 'Nomor'))
       ff = open(self.nfile+'.html', "r+")    
       print(ff.read())

       
class raviDua1184040(Thread):
   def __init__(self, name,threadId,ravi,rahmatul ,nfile):
       Thread.__init__(self)
       self.threadLock = Lock()
       self.semaphore = semaphore
       self.rlock = RLock()
       self.name = name
       self.nfile=os.path.join(os.path.dirname(__file__), nfile)
       self.threadId = threadId
       self.ravi=ravi
       self.rahmatul=rahmatul
      
   def run(self):
       print("\n"+str(self.threadId)+". ---> " + self.name + "Mulai aja ya")
       self.threadLock.acquire()
       print("ini threeadlock acquire utama")
       self.count()
       self.threadLock.release()
       print("\n"+str(self.threadId)+". ---> " + currentThread().getName() + "Finish")
         
   def apicount(self):
       with self.rlock:
           print('Inside rlock apipangkat, akses web service...')
           apiurl='	http://api.mathjs.org/v4/?expr=2%2B3*sqrt(4)'
           eq=str(self.ravi)+'*'+str(self.rahmatul)
           response = requests.get(apiurl+eq)
           html=response.content.decode(response.encoding)
           hasil = int(html)
           string = "Angka : "
           i = 1
           for i in range(1, 11):
               string = string+str(i)
               i = i +1
           self.createfile(string)  
           x = open(self.nfile, "r+")
           print(x.read())

   def count(self):
       with self.rlock:
            self.apicount()
       
   def createfile(self,isi):
       print('Membuat file baru nih : '+ self.nfile)
       f = open(self.nfile, "w")
       f.write(str(isi))
       f.close()
       print('Sudah di buat file baru-nya nih, SIAP-Siap ya, selanjutnya mau relese semaphore')
       self.semaphore.release()
       print('di dalam Semaphore release tadi, semaphore sudah di release')