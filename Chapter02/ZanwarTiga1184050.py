import threading
import requests
import os

event = threading.Event()

class zanwarRewrite (threading.Thread):
   def __init__(self,name, thread_number, filename):
       threading.Thread.__init__(self)  
       self.name = name
       self.threadLock = threading.Lock()
       self.thread_number = thread_number
       self.filename=os.path.join(os.path.dirname(__file__), filename)

   def run(self):
       print("\n"+str(self.thread_number)+". ---> " + self.name + "start.")
       self.threadLock.acquire()
       print('A: Pls give me some motivation :(')
       print('B: Okay, pls wait~')
       event.wait()
       print('rewrite : '+self.filename)
       self.readfile()
       print("Read after rewrite")
       self.rewritefile()
       event.clear()
       self.threadLock.release()
       print("\n"+str(self.thread_number)+". ---> " + threading.currentThread().getName() + "end")

   def readfile(self):
       f = open(self.filename, "r")
       print("File's Content is : \n "+f.read())
      
   def rewritefile(self):
       f = open(self.filename, "r")
       fd = open(self.filename+'.txt', "w")
       for line in f:
           fd.write(line.replace('Quotes', 'Kata Kata Bijak'))
       fd.close()
       fr = open(self.filename+'.txt', "r")    
       print(fr.read())
       fr.close()

       
class zanwarTiga1184050 (threading.Thread):
   def __init__(self, name, thread_number, a ,filename):
       threading.Thread.__init__(self)
       self.threadLock = threading.Lock()
       self.name = name
       self.rlock = threading.RLock()
       self.filename=os.path.join(os.path.dirname(__file__), filename)
       self.thread_number = thread_number
       self.a=a
      
   def run(self):
       print("\n"+str(self.thread_number)+". ---> " + self.name + "start.")
       self.count()
       print("Event Set!")
       event.set()
       print("\n"+str(self.thread_number)+". ---> " + threading.currentThread().getName() + "finish.")
         
   def randomapi(self):
       with self.rlock:
           print('Inside rlock apipangkat, akses web service...')
           apiurl='https://goquotes-api.herokuapp.com/api/v1/random?'
           eq='count='+str(self.a)
           response = requests.get(apiurl+eq)
           html=response.json()
           string = "Quotes : "
           for i in range(len(html["quotes"])):
               hasil = html["quotes"][i]["text"]
               tulis = "\n"+str(i)+". "
               string = string+tulis+str(hasil)
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
       