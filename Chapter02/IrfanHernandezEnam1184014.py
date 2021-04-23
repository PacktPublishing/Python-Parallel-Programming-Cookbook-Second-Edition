from threading import Barrier, Thread
import requests
import os
from time import ctime, sleep

total = 1
nama_minuman = Barrier(total)
file = "Miramas"
filename=os.path.join(os.path.dirname(__file__), file)

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
    x = open(filename, "r")
    print(x.read())
    
def createfile(isi):
    print('Create File : '+ filename)
    f = open(filename, "w")
    f.write(str(isi))
    f.close()
    
def readfile():
    f = open(filename, "r")
    print("Isi Dari File ini : \n "+f.read())
    f.close()

def start():
    api()
    sleep(4)
    readfile()
    print('api dan readfile freached the barrier at: %s \n' % (ctime()))
    nama_minuman.wait()
   
     
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

