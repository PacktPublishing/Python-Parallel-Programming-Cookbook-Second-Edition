from random import randrange
from threading import Barrier, Thread
from time import ctime, sleep
#akan menentukan berapa thread yang akan di tahan untuk diijinkan selesai eksekusi, tengan penanda wait()
# intinya tentukan jumlah thread dan gunakaan wait()
num_runners = 3
finish_line = Barrier(num_runners)
runners = ['Hermawan', 'Dadang', 'Asep']

def runner():
    name = runners.pop()
    waktulari=randrange(2, 5)
    print('Pelari : '+name+str(waktulari)+' detik, ')
    sleep(waktulari)#hanya untuk memberikan jeda waktu random
    finish_line.wait()#tidak akan lanjut ke perintah selanjutnya selama 3(num_runners) thread belum di eksesk
    print('%s reached the barrier at: %s \n' % (name, ctime()))
# In[]:

def main():
    threads = []#buat list kosong namanya threads
    print('START RACE!!!!')
    for i in range(num_runners):#lakukan perulangan sebanyak 3 kali adalah jumlah pelari
        threads.append(Thread(target=runner))#menyimpan objek thread ke dalam variable list threads
        threads[-1].start()#mengambil list thread paling belakang
    for thread in threads:
        thread.join()
    print('Race over!')

#if __name__ == "__main__":
#    main()
