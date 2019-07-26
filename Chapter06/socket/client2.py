import socket
s =socket.socket()
host=socket.gethostname()
port=60000
s.connect((host,port))
s.send('HelloServer!'.encode())
with open('received.txt','wb') as f:
    print ('file opened')
    while True :
        print ('receiving data...')
        data=s.recv(1024)
        if not data:
            break
        print ('Data=>',data.decode())
         # write data to a file
        f.write(data)
f.close()
print ('Successfully get the file')
s.close()
print ('connection closed')
