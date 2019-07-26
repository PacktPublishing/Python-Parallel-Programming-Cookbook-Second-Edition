# client .py
import socket

# create a socket object
s =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# get local machine name
host=socket.gethostname()
port=9999
# connection to hostname on the port .
s.connect((host,port))
# Receive no more than 1024 bytes
tm=s.recv(1024)
s.close()
print ("Time connection server:%s"%tm.decode('ascii'))
