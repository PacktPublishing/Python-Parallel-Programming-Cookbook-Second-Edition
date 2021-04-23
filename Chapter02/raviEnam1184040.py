from threading import Barrier, Thread
import os
import requests
from time import ctime, sleep

no = 1
b = Barrier(no)
r1 = "ravi"
r2 = "newravi"
filename = os.path.join(os.path.dirname(__file__), r1)
filename2 = os.path.join(os.path.dirname(__file__), r2)

def API():
    apiurl='http://www.emsifa.com/api-wilayah-indonesia/api/regencies/13.json'
    response = requests.get(apiurl)
    html=response.json()
    cfile(html)     

def cfile(isi):
    print('File dibuat : '+r1+'.docx \n')
    f = open(filename+".docx", "w")
    print('File dibuat sudah \n')
    f.write(str(isi))
    f.close()
    print('Ini isinya: '+r1+'.docx')
    x = open(filename+".docx", "r")
    print(x.read()+'\n')
    x.close()
    print('Ganti nama \n')
    print('menjadi: '+r2+'.docx \n')
    os.rename(filename+'.docx', filename2+'.docx')
    sleep(2)
    b.wait()
    print('File:'+r1+'.docx'+' berhasil di ganti \n')
    sleep(2)
    b.wait()    
    print('Create, Read, and delete r1: '+r1+' barrier waktu: %s \n' % (ctime()))

def run():
    API()
    sleep(2)
    b.wait()
    print('Semua mencapai barrier pada waktu: %s \n' % (ctime()))

def main():
    threads = []
    print('goodluck')
    for i in range(no):
        threads.append(Thread(target=run))
        threads[-1].start()
    for thread in threads:
        thread.join()
    print('done')
    return True

#if __name__ == "__main__":
#   main() 