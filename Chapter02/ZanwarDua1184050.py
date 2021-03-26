from threading import Thread,currentThread, Lock, RLock, Semaphore
import requests
import os

semaphore = Semaphore(0)
hasilperhitungan=0

class zanwarRewrite (Thread):
   def __init__(self,name,thread_number,filename):
       Thread.__init__(self)    
       self.threadLock = Lock()
       self.name = name
       self.thread_number = thread_number
       self.filename=os.path.join(os.path.dirname(__file__), filename)
       self.semaphore = semaphore

   def run(self):
       print("\n"+str(self.thread_number)+". ---> " + self.name + "start.")
       print('semaphore acquire')
       self.threadLock.acquire()
       self.semaphore.acquire()
       print('rewrite : '+self.filename)
       self.rewritefile()
       self.threadLock.release()
       print("Read setelah rewrite")
       self.readfile()
       print("\n"+str(self.thread_number)+". ---> " + currentThread().getName() + "end")

   def readfile(self):
       f = open(self.filename, "r")
       print("File's Content is : \n "+f.read())
      
   def rewritefile(self):
       f = open(self.filename, "r")
       fd = open(self.filename+'.txt', "w")
       for line in f:
           fd.write(line.replace('Angka : ', ''))
       fr = open(self.filename+'.txt', "r")    
       print(fr.read())

       
class zanwarDua1184050 (Thread):
   def __init__(self, name,thread_number,a,b ,filename):
       Thread.__init__(self)
       self.threadLock = Lock()
       self.semaphore = semaphore
       self.rlock = RLock()
       self.name = name
       self.filename=os.path.join(os.path.dirname(__file__), filename)
       self.thread_number = thread_number
       self.a=a
       self.b=b
      
   def run(self):
       print("\n"+str(self.thread_number)+". ---> " + self.name + "start.")
       self.threadLock.acquire()
       print("main threadlock acquire")
       self.count()
       self.threadLock.release()
       print("\n"+str(self.thread_number)+". ---> " + currentThread().getName() + "finish.")
         
   def randomapi(self):
       with self.rlock:
           print('Inside rlock apipangkat, akses web service...')
           apiurl='https://www.random.org/integers/?num=1&'
           eq='min='+str(self.a)+'&max='+str(self.b)
           form = '&col=1&base=10&format=plain&rnd=new'
           response = requests.get(apiurl+eq+form)
           html=response.content.decode(response.encoding)
           hasil = int(html)
           string = "Angka : "
           i = 1
           while i <= hasil:
               string = string+str(i)
               i = i +1
           self.createfile(string)  
           x = open(self.filename, "r")
           print(x.read())

   def count(self):
       with self.rlock:
            self.randomapi()
       
   def createfile(self,isi):
       print('Create File : '+ self.filename)
       f = open(self.filename, "w")
       f.write(str(isi))
       f.close()
       print('Create File')
       self.semaphore.release()
       print('Semaphore released.')
       