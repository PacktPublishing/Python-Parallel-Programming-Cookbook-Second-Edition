from threading import Barrier, Thread
import requests
from time import ctime, sleep
import os


angka = 1
finish = Barrier(angka)
yuhu = []


def webservices():
	apiurl = 'https://koreanjson.com/users'
	response = requests.get(apiurl)
	html = response.json()
	for i in range(len(html)):
		link = html[i]["username"]
		yuhu.append(link)

	createfile(yuhu)

def readfile():
	f = open("vicky.txt", "r")
	print("File content: " +f.read())
	f.close()


def createfile(isi):
	print('Create File : vicky.txt')
	f = open("vicky.txt", "w")
	f.write(str(isi))
	f.close()

def rename():
	os.rename("vicky.txt", "safira.txt")


def run():
	webservices()
	sleep(3)
	name = yuhu.pop()
	print('%s reached the barrier at: %s \n' % (name, ctime()))
	finish.wait()
	
	readfile()
	rename()


def main():
	baru = []
	print("\n Mulai \n")
	for i in range(angka):
		baru.append(Thread(target=run))
		baru[-1].start()
	for thread in baru:
		thread.join()
	print("Selesai")
	return True

#if __name__ == "__main__":
#    main()
    

