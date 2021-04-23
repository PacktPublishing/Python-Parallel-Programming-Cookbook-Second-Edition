from threading import Barrier, Thread
import os
import requests
from time import ctime, sleep

angka = 1
b = Barrier(angka)
file = "alif"
file2 = "alifbaru"
filename = os.path.join(os.path.dirname(__file__), file)
filename2 = os.path.join(os.path.dirname(__file__), file2)

def getapi():
    apiurl='http://www.emsifa.com/api-wilayah-indonesia/api/provinces.json'
    response = requests.get(apiurl)
    html=response.json()
    handlingfile(html)     

def handlingfile(isi):
    print('Yoo filenya dibuat dulu ya : '+file+'.txt \n')
    f = open(filename+".txt", "w")
    print('Filenya udah dibuat nih \n')
    f.write(str(isi))
    f.close()
    print('Isi filenya apaan yaa: '+file+'.txt')
    x = open(filename+".txt", "r")
    print(x.read()+'\n')
    x.close()
    print('coba ganti nama filenya dong \n')
    print('Rename File menjadi: '+file2+'.txt \n')
    os.rename(filename+'.txt', filename2+'.txt')
    sleep(2)
    b.wait()
    print('File:'+file+'.txt'+' telah berhasil di Rename \n')
    sleep(2)
    b.wait()    
    print('Create, Read, and delete file: '+file+' mencapai barrier pada waktu: %s \n' % (ctime()))

def run():
    getapi()
    sleep(2)
    b.wait()
    print('Semua mencapai barrier pada waktu: %s \n' % (ctime()))

def main():
    threads = []
    print('Gasskeun! Semoga berhasil')
    for i in range(angka):
        threads.append(Thread(target=run))
        threads[-1].start()
    for thread in threads:
        thread.join()
    print('Yeaayy berhasil berhasil! Horeee!')
    return True

#if __name__ == "__main__":
#   main() 