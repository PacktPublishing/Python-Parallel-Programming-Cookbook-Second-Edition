from threading import Thread,currentThread, Lock, RLock, Semaphore
import requests
import os

semaphore = Semaphore(0)
hasilperhitungan=0

class raviSemaphoreDeleteFile (Thread):
   def __init__(self,name,thread_number,namafile):
       Thread.__init__(self)    
       self.threadLock = Lock()
       self.name = name
       self.thread_number = thread_number
       self.namafile=os.path.join(os.path.dirname(__file__), namafile)
       self.semaphore = semaphore

   def run(self):
       print("\n"+str(self.thread_number)+". ---> " + self.name + "jalan") #baris baru, yang pertama (1) jalan, method raviSemaphoreDeleteFile memanggil dari test_app.py  
       print('mau menjalankan semaphore acquire untuk baca dan delete file') #selanjutnya (2) yang dijalankan
       self.threadLock.acquire()
       self.semaphore.acquire()
       print('melakukan baca file : '+self.namafile)  # (11)
       self.readfile()
       print('melakukan rename file : '+self.namafile) # (13.1) bersamaan dengan Thread utama selesai
       self.renamefile()
       self.threadLock.release()
       print("\n"+str(self.thread_number)+". ---> " + currentThread().getName() + "selesai") #threaddelete= raviSemaphoreDeleteFile  Selesai (14)
 
   def readfile(self):
       f = open(self.namafile, "r") #r / read = membuka file untuk dibaca (default).
       f.read(2) #Metode read(n) berfungsi untuk membaca sebanyak n karakter
       print("menampilkan dua angka terakhir 3125: "+f.read()) # (12)
    
   def renamefile(self):
    os.rename(self.namafile,self.namafile+('.croot'))

class raviDua1184040 (Thread):
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
       print("\n"+str(self.thread_number)+". ---> " + self.name + "jalan") #Setelah itu (3) raviDua1184040 jalan
       self.threadLock.acquire()
       print("threeadlock acquire utama") #terus (4)
       self.hitung()
       self.threadLock.release()
       print("\n"+str(self.thread_number)+". ---> " + currentThread().getName() + "selesai") #Thread Utama Selesai (13.1) threadutama = raviDua1184040 
         
   def apipangkat(self):
       with self.rlock:
           print('didalam rlock apipangkat, akses web service...') #Lanjut (6) kesini
           apiurl='https://api.mathjs.org/v4/?expr='
           eq=str(self.a)+'^'+str(self.b)
           response = requests.get(apiurl+eq)
           html=response.content.decode(response.encoding)
           hasil = int(html)
           print("hasil : "+str(hasil)) #ini (7)
           self.createfile(hasil)       

   def hitung(self):
       with self.rlock:
            print('rlock hitung') #Setelah itu (5)
            self.apipangkat()
       
   def createfile(self,isi):
       print('membuat file baru : '+ self.namafile) #Selanjutnya yang ini (8)
       f = open(self.namafile, "w") #Membuka file untuk ditulis. Membuat file baru jika file belum tersedia atau menimpa isi file jika file sudah ada
       f.write(str(isi)) 
       f.close()
       print('sudah membuat file baru, mau relese semaphore') #Lanjut (9)
       self.semaphore.release()
       print('di dalam Semaphore release, semaphore sudah di release') #Setelah itu (10)
       



