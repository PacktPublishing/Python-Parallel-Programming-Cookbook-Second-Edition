# server .py

import socket
port=60000
s =socket.socket()
host=socket.gethostname()
s.bind((host,port))
s.listen(15)
print('Serverlistening....')
while True :
    conn,addr=s.accept()
    print ('Gotconnectionfrom',addr)
    data=conn.recv(1024)
    print ('Serverreceived',repr(data.decode()))
    filename='mytext.txt'
    f =open(filename,'rb')
    l =f.read(1024)
    while (l):
        conn.send(l)
        print ('Sent',repr(l.decode()))
        l =f.read(1024)
        f.close()
        print ('Donesending')
        conn.send('->Thankyouforconnecting'.encode())
        conn.close()
