from threading import Barrier, Thread
from time import ctime, sleep
import requests
import os

jumlah = 1
shield = Barrier(jumlah)
filename = "iraa.txt"
filename2 = "iranew.txt"

def getapi():
    apiurl='https://api.thecatapi.com/v1/images/search'
    response = requests.get(apiurl)
    html=response.json()
    createfile(html)   

def createfile(isi):
    f = open(filename, "w")
    f.write(str(isi))
    f.close()

def read():
    x = open(filename, "r")
    print(x.read())

def renamefile():
    os.rename(filename, filename2)
    print('file sudah direname')

def deletefile():
    os.remove(filename2)
    print('File sudah dihapus')

def runner():
    getapi()
    sleep(2)
    shield.wait()
    sleep(2)
    print('udah mencapai barrier nih : %s \n' % (ctime()))
    shield.wait()
    print('Semua mencapai barrier pada waktunya nih: %s \n' % (ctime()))
    read()
    shield.wait()


def main():
    threads = []
    print('Start!')
    for i in range(jumlah):
        threads.append(Thread(target=runner))
        threads[-1].start()
    for thread in threads:
        thread.join()
    print('Finish!')
    return True

#if __name__ == "__main__":
#    main()