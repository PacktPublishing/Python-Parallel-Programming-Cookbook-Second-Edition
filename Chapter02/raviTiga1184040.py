from threading import Thread,currentThread, Lock, RLock, Event
import requests
import os

items = []
event = Event()
hasilperhitungan=0

class raviMenulis (Thread):
   def __init__(self,name,threadId,nfile):
       Thread.__init__(self)    
       self.threadLock = Lock()
       self.name = name
       self.threadId = threadId
       self.nfile=os.path.join(os.path.dirname(__file__), nfile)
       self.threadEvent = event

   def run(self):
        print("\n"+str(self.threadId)+". ---> " + self.name + "Go")
        self.threadLock.acquire()
        print('Joni: Saya mau Belajar berhitung 1 sampai 10, Jono kamu bisa buatkan saya Angka dan Nomor nya?')
        print('Jono: Bisa dong, tunggu sebentar')
        event.wait()
        print('Menulis : '+self.nfile)
        self.readfile()
        print('Baca file setala ditulis : '+self.nfile)
        self.writefile()
        self.threadEvent.clear()
        self.threadLock.release()
        print("\n"+str(self.threadId)+". ---> " + currentThread().getName() + "Finish")
   
   def readfile(self):
       f = open(self.nfile, "r+")
       ##f.read(20) #Metode read(n) berfungsi untuk membaca sebanyak n karakter.
       print("Ini angkanya, selamat belajar Joni : \n "+f.read())
      
   def writefile(self):
       f = open(self.nfile, "r+")
       fd = open(self.nfile+'.pdf', "w")
       for line in f:
           fd.write(line.replace('Ini Angkanya', 'dan Ini Nomor'))
       fd.close()
       fr = open(self.nfile+'.pdf', "r+")    
       print(fr.read())
       fr.close()

       
class raviTiga1184040(Thread):
   def __init__(self, name,threadId,r,f ,nfile):
       Thread.__init__(self)
       self.threadLock = Lock()
       self.threadEvent = event
       self.rlock = RLock()
       self.name = name
       self.nfile=os.path.join(os.path.dirname(__file__), nfile)
       self.threadId = threadId
       self.r=r
       self.f=f
      
   def run(self):
       print("\n"+str(self.threadId)+". ---> " + self.name + "Mulai")
       self.count()
       print("Event di Set!")
       event.set()
       print("\n"+str(self.threadId)+". ---> " + currentThread().getName() + "finish.")
         
   def Api(self):
       with self.rlock:
           print('Di dalam rlock APIpangkat, akses web service...')
           apiurl='	https://api.mathjs.org/v4/?expr=4%2B2*6-8'
           eq=str(self.r)+'*'+str(self.f)
           response = requests.get(apiurl+eq)
           html=response.content.decode(response.encoding)
           hasil = int(html)
           string = " Angka : "
           i = 1
           for i in range(1, 11):
               isinya = (1, 11)
               items.append(isinya)
               string = string+str(i)
               i = i +1
           self.createfile(string)  
           x = open(self.nfile, "r+")
           print(x.read())
           isinya = (1, 11)
           items.append(isinya)
           

   def count(self):
       with self.rlock:
            self.Api()
       
   def createfile(self,isi):
       print('Create File : '+ self.nfile)
       f = open(self.nfile, "w")
       f.write(str(isi))
       f.close()