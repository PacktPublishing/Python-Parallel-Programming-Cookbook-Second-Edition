from threading import Barrier, Thread
import os
import requests
from time import ctime, sleep

kali = 3
barr = Barrier(kali)
file = "za"
filename = os.path.join(os.path.dirname(__file__), file)

def randomapi():
    apiurl='https://goquotes-api.herokuapp.com/api/v1/random?'
    eq='count='+str(kali)
    response = requests.get(apiurl+eq)
    html=response.json()
    string = "Quotes : "
    for i in range(len(html["quotes"])):
        hasil = html["quotes"][i]["text"]
        tulis = "\n"+str(i)+". "
        string = string+tulis+str(hasil)
    createfile(string)  

def read():
    x = open(filename+'2.txt', "r")
    print(x.read())
    x.close()

def createfile(isi):
       for i in range(kali):
           print('Create File : '+file+str(i)+'.txt')
           f = open(filename+str(i)+".txt", "w")
           f.write(str(isi))
           sleep(2)
           barr.wait()
           print('Read File:'+file+str(i)+'.txt')
           x = open(filename+str(i)+".txt", "r")
           print(x.read())
           x.close()
           print('Create & Read reached the barrier at: %s \n' % (ctime()))
           sleep(2)
           barr.wait()
           f.close()

def run():
    randomapi()
    sleep(2)
    print('Remove 0 reached the barrier at: %s \n' % (ctime()))
    barr.wait()
    print('hapus file pertama!')
    os.remove(filename+'0.txt')
    sleep(2)
    print('Remove 1 reached the barrier at: %s \n' % (ctime()))
    barr.wait()
    print('hapus file kedua!')
    os.remove(filename+'1.txt')
    print('Baca File za2.txt')
    read()

### In[]:

def main():
    threads = []
    print('START!!!!')
    for i in range(kali):
        threads.append(Thread(target=run))
        threads[-1].start()
    for thread in threads:
        thread.join()
    print('Over!')
    return True

#if __name__ == "__main__":
#   main()