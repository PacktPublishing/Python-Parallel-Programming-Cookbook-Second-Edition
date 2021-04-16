# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 12:31:12 2021

@author: Josuansef Pardede (1184091)
"""
from threading import Barrier, Thread
import os
import requests
from time import ctime, sleep

jenis_file = 1
batas = Barrier(jenis_file)
file = "movie_2020_"
filename = os.path.join(os.path.dirname(__file__), file)


def ApiJosuansef1184091():  
        url = "https://movie-database-imdb-alternative.p.rapidapi.com/"
        querystring = {"s":"Avengers Endgame","page":"1","r":"json"}

        headers = {
            'x-rapidapi-key': "03ea4d51b5mshde64ddab3687a71p1fb88fjsn3c194b2ea8bc",
            'x-rapidapi-host': "movie-database-imdb-alternative.p.rapidapi.com"
            }

        response = requests.request("GET", url, headers=headers, params=querystring)
        html=response.json()
        print(response.text)
        Josuansef1184091_CreateAppendFile(html)

def Josuansef1184091_CreateAppendFile(konten):
       for i in range(2):
           print('Create File : '+file+str(i)+'.txt \n')
           f = open(filename+str(i)+".txt", "w+")
           f.write(str(konten))
           f.close()
           
           print('Append File: '+file+str(i)+'.txt')
           a = open(filename+str(i)+".txt", "a+")
           a.write(" => Film Terbaik Sepanjang Masa setelah 'Titanic' %d\r\n")
           a.close()
           print('Create & Append '+file+str(i)+' reached the barrier at: %s \n' % (ctime()))
           sleep(2)
           batas.wait()

def run():
    ApiJosuansef1184091()
    sleep(2)
    batas.wait()
    print('All reached the barrier at: %s \n' % (ctime()))

### In[]:

def main():
    threads = []
    print('MULAI LAH, APA LAGI YEKAN!')
    for i in range(jenis_file):
        threads.append(Thread(target=run))
        threads[-1].start()
    for thread in threads:
        thread.join()
    print('UDAH UDAH! UDAH SELESAI GUYS!')
    return True

#if __name__ == "__main__":
 #main() 