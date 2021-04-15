from threading import Barrier, Thread
import requests
import os
from time import ctime, sleep

total = 1
brr = Barrier(total)
file = "Miramas"
filename=os.path.join(os.path.dirname(file), file)

def api():
    apiurl='https://www.thecocktaildb.com/api/json/v1/1/search.php?s=margarita'
    response = requests.get(apiurl)
    html=response.json()
    string="minuman : " 
    for i in range(len(html["drinks"])):
        hasil = html["drinks"][i]["strDrink"]
        tulis = "\n"+str(i)+". "
        string = string+tulis+str(hasil)
    createfile(string)
 

def createfile(isi):
    print('Create File : '+ filename)
    f = open(filename+".txt", "w")
    f.write(str(isi))
    f.close()
    a = open(filename+".txt", "r")
    print("Isi Dari File ini : \n "+a.read())
    a.close()
    b = open(filename+".txt", "a")
    b.write("\ndiatas adalah minuman yang tersedia")
    b.close()
    c = open(filename+".txt", "r")
    print("Perubahan Isi Dari File ini : \n "+c.read())
    c.close()

def start():
    api()
    sleep(4)
    brr.wait()
    print('API and readfile reached the barrier at: %s \n' % (ctime()))


def main():
    threads = []
    print('Minuman Yang tersedia')
    for i in range(total):
        threads.append(Thread(target=start))
        threads[-1].start()
    for thread in threads:
        thread.join()
    print('Telah Muncul')
    return True
