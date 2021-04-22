from threading import Barrier, Thread
from time import ctime, sleep
import requests

jumlah = 3
shield = Barrier(jumlah)
runners = []
filename = "luffy.txt"
#api ida
def api():
    url = "https://api.jikan.moe/v3/search/anime?q=One%20Piece"
    response = requests.get(url)
    html=response.json()
    string = "Anime: "
    for i in range(len(html)):
        hasil = html["results"][i]["title"]
        data = str(hasil)
        ent = "\n"+str(i)+". "
        string = string+ent+data
        runners.append(data)
    createfile(string)

def read():
    x = open(filename, "r")
    print(x.read())

def createfile(isi):
    f = open(filename, "w")
    f.write(str(isi))
    f.close()
                
def runner():
    api()
    sleep(2)
    shield.wait()
    name = runners.pop()
    sleep(2)
    print('%s sudah mencaapai barier pada: %s \n' % (name, ctime()))
    shield.wait()
    print('Create dan Read File sudah mencaapai barier pada: %s \n' % (ctime()))
    read()
    shield.wait()
    

def main():
    threads = []
    print('Mulai!')
    for i in range(jumlah):
        threads.append(Thread(target=runner))
        threads[-1].start()
    for thread in threads:
        thread.join()
    print('Selesai!')
    return True

#if __name__ == "__main__":
#    main()
