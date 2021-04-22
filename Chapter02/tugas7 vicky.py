from threading import Thread
from queue import Queue
import requests
import os

queue=Queue()
coba=[]
apiurl = 'https://koreanjson.com/users'
response = requests.get(apiurl)
html = response.json()

class vickyqueue(Thread):
    def __init__(self,namathread):
        Thread.__init__(self)
        self.namathread=namathread
        
        
    def webservices(self):
        for i in range(len(html)):
            link = html[i]["username"]
            coba.append(link)
            queue.put(coba)
    
    
    def run(self):
        print("queue mulai \n")
        self.webservices()
        

class vickysafira(Thread):
    def __init__(self,namathread,filename):
        Thread.__init__(self)
        self.namathread=namathread
        self.filename=filename
        
        
    def readfile():
        f = open(self.filename+".txt","r")
        f.close()
    
    
    def createfile(isi):
        print('Create File : '+self.filename)
        f = open(self.filename, "w")
        f.write(str(isi))
        f.close()
    
    
    def hasil(self):
        for j in range(len(html)):
            aku=coba.pop()
            self.createfile()
            queue.get()
            queue.task_done()
        print("baca file"+self.filename+".txt")
        self.readfile()
    
    
    def run(self):
        self.hasil()
        print("selesai")

