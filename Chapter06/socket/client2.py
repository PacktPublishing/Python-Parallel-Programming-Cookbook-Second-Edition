# File transfer client

import socket

s = socket.socket()

host = socket.gethostname()
port = 60000

# Connect to server
s.connect((host, port))

# Send request
s.send('HelloServer!'.encode())

# Save received file
with open('received.txt', 'wb') as f:

    print('file opened')

    while True:

        print('receiving data...')

        data = s.recv(1024)

        if not data:
            break

        print('Data=>', data.decode())

        f.write(data)

print('Successfully get the file')

s.close()

print('connection closed')