# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 18:20:47 2021

@author: HP
"""

from threading import Barrier, Thread
import os
import requests
from time import ctime, sleep

jika = 1
br = Barrier(jika)
file = "list film"
filename = os.path.join(os.path.dirname(__file__), file)

def webapi():
    apiurl='https://bioskop-api-zahirr.herokuapp.com/api/now-playing'
    response = requests.get(apiurl)
    html=response.json()
    buatfile(html)

def buatfile(isi):
    for i in range(1):
       print('buat file dulu gan, namanya : '+file+'.txt \n')
       f = open("Film.txt", "w")
       print('File sudah berhasil dibuat gan \n')
       f.write(str(isi))
       f.close()
       f = open("Film.txt", "r")
       print("ini adalah isi filenya gan: \n" +f.read())   
       print('Create, Read this file: '+file+' mencapai barrier pada waktu: %s \n' % (ctime()))

def jalan():
    webapi()
    sleep(2)
    br.wait()
    print('All reached the barrier at: %s \n' % (ctime()))

### In[]:

def main():
    threads = []
    print('Bentar Gann')
    for i in range(jika):
        threads.append(Thread(target=jalan))
        threads[-1].start()
    for thread in threads:
        thread.join()
    print('Over!')
    return True

#if __name__ == "__main__":
#   main() 