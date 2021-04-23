# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 13:48:09 2021

@author: Rizaluardi
"""
from threading import Barrier, Thread
import os
import requests
from time import ctime, sleep

kpos = 5
bar = Barrier(kpos)
file = "list kodepos"
filename = os.path.join(os.path.dirname(file), file)

def webapiservice():
    apiurl=' https://kodepos-2d475.firebaseio.com/list_propinsi.json?print=pretty'
    response = requests.get(apiurl)
    html=response.json()
    buatkodepos(html)

def buatkodepos(isi):
   for i in range(1):
    print('Sebentar sedang membuat file bernama : '+file+'.txt \n')
    k = open("Kodepos.txt", "w")
    print('Oke file telah dibuat \n')
    k.write(str(isi))
    k.close()
    k = open("Kodepos.txt", "r")
    print("Berikut adalah data kodeposnya : \n" +k.read())
    print('Create, Read this file: '+file+' telah mencapai barrier pada waktu: %s \n' % (ctime()))

def eksekusi():
    webapiservice()
    sleep(2)
    bar.wait()
    print('All reached the barrier at: %s \n' % (ctime()))

### In[]:

def main():
    threads = []
    print('Tunggu sejenak')
    for i in range(kpos):
        threads.append(Thread(target=eksekusi))
        threads[-1].start()
    for thread in threads:
        thread.join()
    print('Over!')
    return True

#if __name__ == "__main__":
#   main()