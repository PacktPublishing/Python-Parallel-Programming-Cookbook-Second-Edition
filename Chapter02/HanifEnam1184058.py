from threading import Barrier, Thread
import os
import requests
from time import ctime, sleep

bar = Barrier(1)
file = "pokemon"
filename = os.path.join(os.path.dirname(__file__), file)

def createfile(isi):
    print('Buat file : '+file+'.txt \n')
    f = open(filename+".txt", "w")
    f.write(str(isi))
    f.close()
    print('Membaca file: '+file+'.txt \n')
    x = open(filename+".txt", "r")
    print(x.read()+'\n')
    x.close()
    print("Copy file ke direktori luar")
    copyfile()
    print('Membuat, membaca dan copy '+file+' menggapai barrier dalam: %s \n' % (ctime()))
    sleep(2)
    bar.wait()
    
def copyfile():
    with open ("F:\\Kuliah\\Semester 6\\Sistem Tersebar\\Python-Parallel-Programming-Cookbook-Second-Edition\\Chapter02\\pokemon.txt", "rb") as read:
        with open ("F:\\Kuliah\\Semester 6\\Sistem Tersebar\\Python-Parallel-Programming-Cookbook-Second-Edition\\pokemon_copy.txt", "wb") as filetobecopied:
            filetobecopied.write(read.read())
    
def randomapi():
    print('akses web service...')
    apiurl='https://pokeapi.co/api/v2/pokemon/ditto'
    response = requests.get(apiurl)
    html=response.json()
    string = "ability :"
    for i in range(len(html["abilities"])):
        hasil = html["abilities"][i]["ability"]["name"]
        tulis = "\n"+str(i)+". "
        string = string+tulis+str(hasil)
    createfile(string)
        
def run():
    randomapi()
    sleep(2)
    bar.wait()
    print('All reached the barrier at: %s \n' % (ctime()))

def main():
    threads = []
    print('\nBismillah berkah Ramadhan \n')
    for i in range(1):
        threads.append(Thread(target=run))
        threads[-1].start()
    for thread in threads:
        thread.join()
    print('Alhamdulillah bisa')
    return True
