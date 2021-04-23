# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 14:20:29 2021

@author: Okky Yudistira
"""

from threading import Thread
from queue import Queue
import requests
import os
import threading

queue = Queue()
person = []
event = threading.Event()

class Person(threading.Thread):
    def __init__(self, name, thread_number, filename):
        Thread.__init__(self)
        self.name = name
        self.thread_number = thread_number
        self.filename = os.path.join(os.path.dirname(__file__), filename)
    
    def run(self):
        print("\n"+str(self.thread_number)+". ---> " + self.name + "Mulai")
        self.event.wait()
        self.threadLock.acquire()
        print('melakukan baca file : '+self.namafile)
        self.readfile()
        self.event.wait()
        self.threadLock.release()
        print("\n"+str(self.thread_number)+". ---> " +  threading.currentThread().getName() + "Membaca file telah selesai")
        print ("menjalankan event clear")
        self.event.clear()
       
    def readfile(self):
        queue.get()
        f = open(self.namafile, "r")
        print("Membaca isi file pada program Okky7 : "+f.read())
        queue.task_done()
       
class okky(threading.Thread):
    def __init__(self, name, thread_number, a ,filename):
        threading.Thread.__init__(self)
        self.threadLock = threading.Lock()
        self.name = name
        self.rlock = threading.RLock()
        self.filename=os.path.join(os.path.dirname(__file__), filename)
        
    def run(self):
        print("\n" + self.name + "Start!")
        self.result()
        g = queue.get()
        print("\n Queue. . .")
        print(g)
        queue.task_done()
        event.set()
        print("\n" + threading.currentThread().getName() + "End.")
        
    def api(self):
        with self.rlock:
            print('Webservice Random User')
            apiurl='https://randomuser.me/api'
            response = requests.get(apiurl)
            html=response.json()
            queue.put(html)
            self.createfile(html)
    
    def result(self):
        with self.rlock:
            self.api()
       
    def createfile(self,isi):
        print('Create File : '+ self.filename)
        f = open(self.filename, "w")
        f.write(str(isi))
        f.close()