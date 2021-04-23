from threading import Barrier, Thread
import os
import requests
from time import ctime, sleep

kali = 1
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

def createfile(isi):
       for i in range(3):
           print('Create File : '+file+str(i)+'.txt \n')
           f = open(filename+str(i)+".txt", "w")
           f.write(str(isi))
           f.close()
           print('Read File: '+file+str(i)+'.txt')
           x = open(filename+str(i)+".txt", "r")
           print(x.read()+'\n')
           x.close()
           print('Create & Read '+file+str(i)+' reached the barrier at: %s \n' % (ctime()))
           sleep(2)
           barr.wait()
           
def run():
    randomapi()
    sleep(2)
    barr.wait()
    print('All reached the barrier at: %s \n' % (ctime()))

### In[]:

def main():
    threads = []
    print('START!')
    for i in range(kali):
        threads.append(Thread(target=run))
        threads[-1].start()
    for thread in threads:
        thread.join()
    print('Over!')
    return True

#if __name__ == "__main__":
#   main()