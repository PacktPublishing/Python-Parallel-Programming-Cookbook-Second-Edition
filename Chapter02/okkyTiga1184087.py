# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 08:34:57 2021

@author: Okky Yudistira
"""
import threading
import time
import os
import condition
import logging
import items
from flask import request, jsonify
import sqlite3


class okky1184087Write_Trier(threading.Thread):
    def __init__(self,name, thread_number, filename):
       threading.Thread.__init__(self)  
       self.name = name
       self.threadLock = threading.Lock()
       self.thread_number = thread_number
       self.filename=os.path.join(os.path.dirname(__file__), filename)
        
    def start_server():
  # starting server
      print("starting the server...")
  # do some startup work
      time.sleep(2)
  
    def server(b):
        start_server()
        b.wait()
        print("Server is ready.")
        
    def client(b):
        print("waiting for server getting ready...")
        b.wait()
        print("sending request to server...")
        
    if __name__=='__main__':
        b = threading.Barrier(2, timeout=5)
        s = threading.Thread(target=server, args=(b,))
        s.start()
        c = threading.Thread(target=client, args=(b,))
        # client thread
        c.start()
        s.join()
        c.join()
        print("Done")
        
    def trying(self):
        with condition:
            f = open("okky.txt", "w+")
            for i in range(10):
                f.write("hi are you okay number %d\r\n" % (i+1))
            
            if len(items) == 0:
                logging.info('no items to consume')
                
                condition.wait()
                items.pop()
                logging.info('consumed 1 item')
                
                condition.notify()
    
    def run(self):
        for i in range(20):
            time.sleep(2)
            self.trying()

class okky1184087(threading.Thread):
    def __init__(self, name, thread_number, a ,filename):
        threading.Thread.__init__(self)
        self.threadLock = threading.Lock()
        self.name = name
        self.rlock = threading.RLock()
        self.filename=os.path.join(os.path.dirname(__file__), filename)
        self.thread_number = thread_number
        self.a=a
        
        
    def api_filter():
        query_parameters = request.args
        id = query_parameters.get('id')
        published = query_parameters.get('published')
        author = query_parameters.get('author')
        
        query = "SELECT * FROM books WHERE"
        to_filter = []
        
        if id:
            query += ' id=? AND'
            to_filter.append(id)
            
            if published:
                query += ' published=? AND'
                to_filter.append(published)
                
                if author:
                    query += ' author=? AND'
                    to_filter.append(author)
                    
                    if not (id or published or author):
                        
                        return page_not_found(404)
                    
                    query = query[:-4] + ';'
                    conn = sqlite3.connect('books.db')
                    conn.row_factory = dict_factory
                    cur = conn.cursor()
                    results = cur.execute(query, to_filter).fetchall()
                    return jsonify(results)
                
    def createfile(self,isi):
        print('Create File : '+ self.filename)
        f = open(self.filename, "w")
        f.write(str(isi))
        f.close()