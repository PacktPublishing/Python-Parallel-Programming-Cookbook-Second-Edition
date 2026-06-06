# Basic TCP socket client

import socket

# Create client socket
s = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

host = socket.gethostname()
port = 9999

# Connect to server
s.connect((host, port))

# Receive data
tm = s.recv(1024)

s.close()

print(
    "Time connection server:%s"
    % tm.decode('ascii')
)