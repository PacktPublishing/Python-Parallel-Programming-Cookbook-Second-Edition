from threading import Thread,currentThread, Lock, RLock, Event
import requests
import os

items = []
event = Event()
hasilperhitungan=0

class ravieventwriteFile (Thread):
   def __init__(self,name,threadId,nfile):
       Thread.__init__(self)    
       self.threadLock = Lock()
       self.name = name
       self.threadId = threadId
       self.nfile=os.path.join(os.path.dirname(__file__), nfile)
       self.threadEvent = event

   def run(self):
        a=0
    #    while True:
        print("\n"+str(self.threadId)+". ---> " + self.name + "Mulai ya!")
        print('mau menjalankan event wait untuk baca dan tulis, buat ulang file')
        self.threadLock.acquire()
        # self.threadEvent.wait()
    #    while True:
            # time.sleep(2)
        print('Thread Utama raviTiga1184040 : menunggu event set dari ravieventwriteFile, status event.wait')
        event.wait() #menunggu jika event=False / jika event=true maka event jalan
        isinya=items.pop()
        print(str(a)+'. raviTiga1184040: sudah di pop,tumpukan list sebanyak : '+str(len(items))+' isinya : '+str(isinya))
        a = a + 1
        print('raviTiga1184040 : event clear')
            # logging.info('Consumer notify: {} popped by {}'.format(item, self.name))
        # event.clear() # set event=false
            #  items = items.pop()
        # print('baca file dong : '+self.nfile)
        # self.readfile()
        print('Tulis dan buat ulang file dong : '+self.nfile)
        # self.writefile()
        # self.threadLock.release()
        # self.event.clear()
        print("\n"+str(self.threadId)+". ---> " + currentThread().getName() + "Finish")
        # a=a+1
        # print('Konsumer : event clear')
        self.threadLock.release()
        self.threadEvent.clear()

   def readfile(self):
       f = open(self.nfile, "r+")
       ##f.read(20) #Metode read(n) berfungsi untuk membaca sebanyak n karakter.
       print("Tampilin angkanya dong biar kita tau : \n "+f.read())
      
   def writefile(self):
       f = open(self.nfile, "r+")
       fc = open(self.nfile+'.html', "w")
       for line in f:
           fc.write(line.replace('Angka', 'Nomor'))
       ff = open(self.nfile+'.html', "r+")    
       print(ff.read())

       
class raviTiga1184040(Thread):
   def __init__(self, name,threadId,r,f ,nfile):
       Thread.__init__(self)
       self.threadLock = Lock()
       self.threadEvent = event
       self.rlock = RLock()
       self.name = name
       self.nfile=os.path.join(os.path.dirname(__file__), nfile)
       self.threadId = threadId
       self.r=r
       self.f=f
      
   def run(self):
       print("\n"+str(self.threadId)+". ---> " + self.name + "Mulai aja ya")
       self.threadLock.acquire()
    #    for i in range(2):
    #         item = (1, 10)
            # items.append(item)
            # event.set()
            # event.clear()
       print("ini threadlock acquire utama")
       self.count()
       self.threadLock.release()
       print("\n"+str(self.threadId)+". ---> " + currentThread().getName() + "Finish")
         
   def apicount(self):
       with self.rlock:
           print('Dalam rlock apipangkat, akses web service...')
           apiurl='	http://api.mathjs.org/v4/?expr=2%2B3*sqrt(4)'
           eq=str(self.r)+'*'+str(self.f)
           response = requests.get(apiurl+eq)
           html=response.content.decode(response.encoding)
           hasil = int(html)
           string = " Angka : "
           i = 1
           for i in range(1, 11):
               isinya = (1, 11)
               items.append(isinya)
               string = string+str(i)
               i = i +1
           self.createfile(string)  
           x = open(self.nfile, "r+")
           print(x.read())
           isinya = (1, 11)
           items.append(isinya)
        #    self.event.set()
           

   def count(self):
       with self.rlock:
            self.apicount()
       
   def createfile(self,isi):
       print('Buat file baru ya di : '+ self.nfile)
       f = open(self.nfile, "w")
       f.write(str(isi))
       f.close()
       print('Done pembuatan file baru, Bersiaplah, Selanjutnya nih kite mau set event')
       self.threadEvent.set()
    #    self.event.clear()
       print('di dalam event set tadi, event sudah di set ya')