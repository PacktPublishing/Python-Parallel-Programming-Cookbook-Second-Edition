# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 05:28:16 2021

@author: NITRO 5 ACER
"""

import threading
import time
import random
import requests

br=threading.Barrier(2)

def webservices():
    apiurl = 'https://pokeapi.co/api/v2/pokemon/pikachu'
    response = requests.get(apiurl)
    html = response.json()
    print(html["weight"])
    
    
def run():
    webservices()
    br.wait()
    
def main():
    
    threads = []
    
    for i in range(4):
      thread = threading.Thread(target=run)
      thread.start()
      threads.append(thread)
    
    for t in threads:
      t.join() 
    return True 



    
    
    