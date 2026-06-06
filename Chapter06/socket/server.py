# Basic TCP socket server

import socket
import time

# Create server socket
serversocket = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

host = socket.gethostname()
port = 9999

# Bind socket to address
serversocket.bind((host, port))

# Start listening for connections
serversocket.listen(5)

while True:

    # Accept client connection
    clientsocket, addr = serversocket.accept()

    print(
        "Connected with [addr],[port] %s"
        % str(addr)
    )

    # Send current server time
    currentTime = (
        time.ctime(time.time()) + "\r\n"
    )

    clientsocket.send(
        currentTime.encode('ascii')
    )

    clientsocket.close()