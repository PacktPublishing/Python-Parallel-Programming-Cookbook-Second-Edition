from threading import Barrier, Thread
import os
import requests
from time import ctime, sleep

angka = 1
b = Barrier(angka)
file = "parhan"
filename = os.path.join(os.path.dirname(__file__), file)

def apiwebservice():
    apiurl='https://api.kawalcorona.com/indonesia'
    response = requests.get(apiurl)
    html=response.json()
    manajemenfile(html)     

def manajemenfile(isi):
    print('buat file terlebih dahulu : '+file+'.txt \n')
    f = open(filename+".txt", "w")
    print('File telah berhasil dibuat \n')
    f.write(str(isi))
    f.close()
    print('Isi file tersebut adalah: '+file+'.txt')
    x = open(filename+".txt", "r")
    print(x.read()+'\n')
    x.close()
    print('coba hapus file \n')
    print('Hapus File: '+file+'.txt \n')
    os.remove(filename+'.txt')
    sleep(2)
    b.wait()
    print('File:'+file+'.txt'+' telah berhasil di Hapus \n')
    sleep(2)
    b.wait()    
    print('Create, Read, and delete file: '+file+' mencapai barrier pada waktu: %s \n' % (ctime()))

def run():
    apiwebservice()
    sleep(2)
    b.wait()
    print('Semua mencapai barrier pada waktu: %s \n' % (ctime()))

def main():
    threads = []
    print('Semoga berhasil')
    for i in range(angka):
        threads.append(Thread(target=run))
        threads[-1].start()
    for thread in threads:
        thread.join()
    print('Success')
    return True

# if __name__ == "__main__":
#   main() 