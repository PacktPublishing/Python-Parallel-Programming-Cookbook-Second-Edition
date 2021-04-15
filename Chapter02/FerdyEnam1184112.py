from threading import Barrier, Thread
import requests
from time import ctime, sleep

nomor = 1
finish = Barrier(nomor)
yuhu = []



def webservice():
    apiurl='https://www.thecocktaildb.com/api/json/v1/1/list.php?c=list'
    response = requests.get(apiurl)
    html=response.json()
    for i in range(len(html["drinks"])):
        cocokin = html["drinks"][i]
        yuhu.append(cocokin)


def bacafile():
    f = open("barrier.txt", "r")
    print("isi file setelah di pop: \n" +f.read())

def utama():
    webservice()
    sleep(2)
    name = yuhu.pop()
    print('%s reached the barrier at: %s \n' % (name, ctime()))
    finish.wait()
    print('buat file baru namanya: barrier.txt \n')
    f = open("barrier.txt","w")
    f.write(str(yuhu))
    f.close()
    bacafile()


def main ():
    hiya=[]
    print("\n Barrier Mulai \n")
    for i in range(nomor):
        hiya.append(Thread(target=utama))
        hiya[-1].start()
    for thread in hiya:
        thread.join()
    print("finish")
    return True



#if __name__ == "__main__":
#    main()

