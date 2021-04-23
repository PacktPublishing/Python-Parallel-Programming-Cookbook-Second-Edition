# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 21:39:32 2021

@author: Rizaluardi
"""
import threading
import requests
import os
from queue import Queue

queue = Queue()
event = threading.Event()

class RizaluardiIms(threading.Thread):
    def __init__(self,name,filename):
        threading.Thread.__init__(self)
        self.name = name
        self.threadLock = threading.Lock()
        self.filename = os.path.join(os.path.dirname(__file__), filename)
        
    def run(self):
        print("\n" + self.name + "mulai.")
        self.threadLock.acquire()
        print('Nama_Provinsi_Di_Indonesia')
        event.wait()
        print('ubah : '+self.filename)
        self.bacafile()
        print("data provinsi berubah")
        self.buatfile()
        event.clear()
        self.threadLock.release()
        print("\n" + threading.currentThread().getName() + "bekerja!")
        
    def bacafile(self):
        f = open(self.filename, "r")
        print("isi filenya : \n "+f.read())
        
    def buatfile(self):
        f = open(self.filename, "r")
        buat = open(self.filename+'.txt', "w")
        for line in f:
            buat.write(line.replace('provinsi', 'nama'))
        buat.close()
        new = open(self.filename+'.txt', "r")
        print(new.read())
        new.close()
        
class RizaluardiTujuh1184102(threading.Thread):
    def __init__(self, name, filename):
        threading.Thread.__init__(self)
        self.name = name
        self.rlock = threading.RLock()
        self.filename = os.path.join(os.path.dirname(__file__), filename)
        
    def run(self):
        print("\n"+ self.name + " mulai.")
        self.main()
        qj = queue.get()
        print("\n antrian queuenya")
        print(qj)
        queue.task_done()
        event.set()
        print("\n" + threading.currentThread().getName() + "selesai.")
    
    def webapiprovinsi(self):
        with self.rlock:
            print('Webservice Api Jadwal Imsyak')
            apiurl='https://dev.farizdotid.com/api/daerahindonesia/provinsi'
            response = requests.get(apiurl)
            html=response.json()
            string = ""
            for i in range(len(html["provinsi"])):
                baru = html["provinsi"][i]
                new = "\n"+str(i)+". "
                string = string+new+str(baru)
            queue.put(string)
            self.createfile(string)
            
    def main(self):
        with self.rlock:
            self.webapiprovinsi()
    
    def createfile(self,isi):
        print('Create File : '+ self.filename)
        f = open(self.filename, "w")
        f.write(str(isi))
        f.close()
        
        