from threading import Barrier, Thread
import requests
from time import ctime, sleep

num_list = 1
list_cocktail = Barrier(num_list)
file = []
filename = "list_cocktail.txt"

def api():
    apiurl ='https://www.thecocktaildb.com/api/json/v1/1/list.php?a=list'
    response = requests.get(apiurl)
    html=response.json()
    string ="list: "
    for i in range(len(html)):
        hasil =html["drinks"]
        tulis = "\n"+str(i)+". "
        string = string+tulis+str(hasil)
    createfile(string)  
    x = open(filename, "r")
    print(x.read())
    

    
def createfile(isi):
    f = open(filename, "w")
    f.write(str(isi))
    f.close()
    
def read():
    x = open(filename, "r")
    print(x.read())
    x.close()
    
def start():
    api()
    sleep(2)
    list_cocktail.wait()
    sleep(2)
    print(' ini barrier nya : %s \n' % (ctime()))
    list_cocktail.wait()
    print('Create dan Read File Barrier: %s \n' % (ctime()))
    read()
    list_cocktail.wait()
    
def main():
    threads = []
    print('Ayo Mulai')
    for i in range(num_list):
        threads.append(Thread(target=start))
        threads[-1].start()
    for thread in threads:
        thread.join()
    print('Udah Selasi')
    return True

#if __name__ == "__main__":
#    main()
    

    

