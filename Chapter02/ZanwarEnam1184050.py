from threading import Barrier, Thread
import os
import requests
from time import ctime, sleep

#akan menentukan berapa thread yang akan di tahan untuk diijinkan selesai eksekusi, tengan penanda wait()
# intinya tentukan jumlah thread dan gunakaan wait()
num_runners = 3
finish_line = Barrier(num_runners)
#runners = ['Hermawan', 'Dadang', 'Asep']
file = "za"
filename = os.path.join(os.path.dirname(__file__), file)

def randomapi():
    apiurl='https://goquotes-api.herokuapp.com/api/v1/random?'
    eq='count='+str(num_runners)
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
       for i in range(num_runners):
           print('Create File : '+file+str(i)+'.txt')
           f = open(filename+str(i)+".txt", "w")
           f.write(str(isi))
           sleep(2)
           finish_line.wait()
           print('Read File:'+file+str(i)+'.txt')
           x = open(filename+str(i)+".txt", "r")
           print(x.read())
           x.close()
           print('Create & Read reached the barrier at: %s \n' % (ctime()))
           sleep(2)
           finish_line.wait()
           f.close()

def runner():
    randomapi()
    sleep(2)
    print('Remove 0 reached the barrier at: %s \n' % (ctime()))
    finish_line.wait()
    print('hapus file pertama!')
    os.remove(filename+'0.txt')
    sleep(2)
    print('Remove 1 reached the barrier at: %s \n' % (ctime()))
    finish_line.wait()
    print('hapus file kedua!')
    os.remove(filename+'1.txt')
    print('Baca File za2.txt')
    read()

### In[]:

def main():
    threads = []#buat list kosong namanya threads
    print('START!!!!')
    for i in range(num_runners):#lakukan perulangan sebanyak 3 kali adalah jumlah pelari
        threads.append(Thread(target=runner))#menyimpan objek thread ke dalam variable list threads
        threads[-1].start()#mengambil list thread paling belakang
    for thread in threads:
        thread.join()
    print('Over!')
    return True

#if __name__ == "__main__":
#   main()