# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 15:11:37 2021

@author: Okky Yudistira
"""
from threading import Barrier, Thread
import os
import requests
from time import ctime, sleep

number = 1
br = Barrier(number)
fl1 = "Random user"
fln1 = os.path.join(os.path.dirname(__file__), fl1)


def api():
    apiurl='https://randomuser.me/api'
    response = requests.get(apiurl)
    html= response.json()
    manajemen(html)
    
def manajemen(isi):
    print('buat file terlebih dahulu : '+fl1+'.txt \n')
    f = open(fln1+".txt", "w")
    print('File telah berhasil dibuat bruh\n')
    f.write(str(isi))
    f.close()
    print('Isi file tersebut adalah: '+fl1+'.txt')
    x = open(fln1+".txt", "r")
    print(x.read()+'\n')
    x.close()
    print('coba Hapus file \n')
    print('Menghapus File: '+fl1+'.txt \n')
    os.remove(fln1+'.txt')
    sleep(1)
    br.wait()
    print('File:'+fl1+'.txt'+' ini telah berhasil di Hapus \n')
    sleep(1)
    br.wait()    
    print('Create, Read, and delete file: '+fl1+' mencapai barrier pada waktu: %s \n' % (ctime()))
    
def run():
    api()
    sleep(1)
    br.wait()
    print('All reached the barrier at: %s \n' % (ctime()))
    
def main():
    threads = []
    print('Mulai Mas!')
    for i in range(number):
        threads.append(Thread(target=run))
        threads[-1].start()
    for thread in threads:
        thread.join()
        print('Berakhir')
        return True

#if __name__ == "__main__":
#   main()