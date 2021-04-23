from threading import Thread,currentThread, Lock, RLock, Event
import requests
import os
from queue import Queue 

queue = Queue()
event = Event()

class Director (Thread):
   def __init__(self,name,thread_number,idafile):
	   Thread.__init__(self)    
	   self.threadLock = Lock()
	   self.name = name
	   self.thread_number = thread_number
	   self.idafile=os.path.join(os.path.dirname(__file__), idafile)
	   self.event = event

   def run(self):
	   print("\n"+str(self.thread_number)+". ---> " + self.name + "jalan")
	   print('class Director mau menjalankan event wait dilanjutkan clear untuk baca dan rename file')
	   self.event.wait()
	   self.threadLock.acquire()
	   print('read file kamu: '+self.idafile)
	   self.readfile()
	   print('rename file kamu: '+self.idafile)
	   self.renamefile()
	   self.event.wait()
	   self.threadLock.release()
	   print("\n"+str(self.thread_number)+". ---> " + currentThread().getName() + "Baca file dan delete file selesai")
	   print ("menjalankan event clear")
	   self.event.clear()

   def readfile(self):
	   ida=queue.get()
	   f = open(self.idafile, "r")
	   print("Isi Filenya apa hayo : "+f.read())
	   print("Sudah selesai baca isi file nya yaw, jalanin queue task done \n")
	   queue.task_done()
	  
   def renamefile(self):
	   print('coba ganti nama filenya dulu dong \n')
	   os.rename(self.idafile,self.idafile+'.txt')
	   print("nama file udah diganti yaww \n")
	
class idaTujuh1184113 (Thread):
   def __init__(self, name,thread_number,a,b ,idafile):
	   Thread.__init__(self)
	   self.threadLock = Lock()
	   self.event = event
	   self.rlock = RLock()
	   self.name = name
	   self.idafile=os.path.join(os.path.dirname(__file__), idafile)
	   self.thread_number = thread_number
	   self.a=a
	   self.b=b
	  
   def run(self):
	   print("\n"+str(self.thread_number)+". ---> " + self.name + "jalan")
	   self.threadLock.acquire()
	   print("threeadlock acquire utama")
	   self.hitung()
	   self.event.set()
	   print('class idaTujuh1184113 sudah selesai melakukan event set')
	   self.threadLock.release()
	   print("\n"+str(self.thread_number)+". ---> " + currentThread().getName() + "selesai")
		 
   def getapi(self):
	   with self.rlock:     
		   print('akses web service...')
		   apiurl = "https://api.jikan.moe/v3/search/anime?q=One%20Piece"
		   response = requests.get(apiurl)
		   html=response.json()
		   string = "Anime: "
		   for i in range(len(html)):
			   hasil = html["results"][i]["title"]
			   data = str(hasil)
			   ent = "\n"+str(i)+". "
			   string = string+ent+data
		   queue.put(string)
		   self.createfile(string)  

   def hitung(self):
	   with self.rlock:
		    print('rlock hitung')
		    self.getapi()
	   
   def createfile(self,isi):
	   print('file baru kamu: '+ self.idafile)
	   f = open(self.idafile, "x")
	   f.write(str(isi))
	   f.close()
	   print('sudah membuat file baru, mau menjalankan event set')
	   
