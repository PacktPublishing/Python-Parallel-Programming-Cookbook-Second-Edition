import threading
import requests
import os

event = threading.Event()

class hanifRename (threading.Thread):
   def __init__(self,name, thread_number, filename):
       threading.Thread.__init__(self)  
       self.name = name
       self.threadLock = threading.Lock()
       self.thread_number = thread_number
       self.filename=os.path.join(os.path.dirname(__file__), filename)

   def run(self):
       print("\n"+str(self.thread_number)+". ---> " + self.name + "start.")
       self.threadLock.acquire()
       print('Menunggu event')
       event.wait()
       print('Nama setelah rename: '+self.filename)
       self.readfile()
       print("Baca file setelah rename")
       self.rewritefile()
       event.clear()
       self.threadLock.release()
       print("\n"+str(self.thread_number)+". ---> " + threading.currentThread().getName() + "end")

   def readfile(self):
       f = open(self.filename, "r")
       print("File's Content is : \n "+f.read())
       f.close()
      
   def rewritefile(self):
       os.rename(self.filename, self.filename+'.docx')
          
class hanifTiga1184058 (threading.Thread):
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
       print("Even set")
       event.set()
       print("\n"+str(self.thread_number)+". ---> " + threading.currentThread().getName() + "finish.")
         
   def randomapi(self):
       with self.rlock:
           print('akses web service...')
           apiurl='https://pokeapi.co/api/v2/pokemon/ditto'
           response = requests.get(apiurl)
           html=response.json()
           string = "ability :"
           for i in range(len(html["abilities"])):
               hasil = html["abilities"][i]["ability"]["name"]
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
       
       
       

