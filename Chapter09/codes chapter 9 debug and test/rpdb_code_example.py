import threading
import rpdb

#debugger = rpdb.Rpdb(port=4444)
rpdb.Rpdb().set_trace()

def my_func(thread_number):
    return print('my_func called by thread N°{}'.format(thread_number))

def main():
    threads = []
    for i in range(10):
        t = threading.Thread(target=my_func, args=(i,))
        threads.append(t)
        t.start()
        t.join()

if __name__ == "__main__":

   main()
 
