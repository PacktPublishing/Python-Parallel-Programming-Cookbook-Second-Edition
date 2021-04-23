from threading import Thread,currentThread, Lock, RLock, Semaphore
import requests
import os

semaphore = Semaphore(0)

class WahyuKurniaSariSemaphoreDeleteFile (Thread):
	def __init__(self,name,threadNumber,filename):
		Thread.__init__(self)	 
		self.lock = Lock()
		self.name = name
		self.threadNumber = threadNumber
		self.filename = filename
		self.filelocation=os.path.join(os.path.dirname(__file__), filename)
		self.semaphore = semaphore

	def run(self):
		print("\n"+str(self.threadNumber)+". menjalankan " + self.name )
		self.lock.acquire()
		self.readAndRename()
		self.lock.release()
		print("\n"+str(self.threadNumber)+". " + currentThread().getName() + " selesai")

	def readAndRename(self):
		self.semaphore.acquire()
		self.renamefile()
		
	def renamefile(self):
		os.rename(self.filelocation,self.filelocation+'.txt')
	 
class WahyuKurniaSariDua1184001 (Thread):
	def __init__(self, name,threadNumber, pokemon,filename):
		Thread.__init__(self)
		self.lock = Lock()
		self.semaphore = semaphore
		self.rlock = RLock()
		self.name = name
		self.pokemon = pokemon
		self.filename = filename
		self.filelocation=os.path.join(os.path.dirname(__file__), filename)
		self.threadNumber = threadNumber
		
	def run(self):
		print("\n"+str(self.threadNumber)+". menjalankan " + self.name )
		self.lock.acquire()
		self.getWeight()
		self.lock.release()
		print("\n"+str(self.threadNumber)+". " + currentThread().getName() + " selesai")

	def getWeight(self):
		with self.rlock:
			print("mencari pokemon : " + self.pokemon)
			apiurl='https://pokeapi.co/api/v2/pokemon/'+self.pokemon
			response = requests.get(apiurl)
			try:
				html=response.json()
				hasil = html["weight"]
				print(self.pokemon+" ditemukan, pokemon ini memiliki berat "+ str(hasil))
			except:
				print(self.pokemon+" tidak ditemukan")
				hasil = "0"
			self.createFile(hasil)
			self.readFile()

	def readFile(self):
		f = open(self.filelocation, "r")
		print("Isi Filenya : "+f.read())
		self.semaphore.release()

	def createFile(self,isi):
		print('membuat file baru "'+ self.filename +'"')
		f = open(self.filelocation, "x")
		f.write(str(isi))
		f.close()


	def getFileLocation(self):
		return self.filelocation+".txt"
		  
	def getFileContent(self):
		 f = open(self.filelocation+".txt", "r")
		 return int(f.read())	





