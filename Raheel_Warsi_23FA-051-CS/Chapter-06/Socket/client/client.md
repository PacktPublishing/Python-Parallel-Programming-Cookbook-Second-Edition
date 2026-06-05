# TCP Socket Client in Python

## Description
This code demonstrates a simple TCP client that connects to a server, receives data, and displays it.

## What This Code Does
- Creates a TCP socket  
- Connects to a server using hostname and port number  
- Receives data from the server  
- Closes the connection  
- Prints the received message (current time from server)  

## Execution Flow
1. Create a TCP socket using:
   ```python
   socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   ```
2. Get local machine hostname  
3. Connect to server on port `9999`  
4. Receive up to 1024 bytes of data  
5. Close socket connection  
6. Decode received data and print output  

## How to Execute
1. Start the socket server first  
2. Open terminal in this folder  
3. Run:
   ```bash
   python client.py
   ```

## End Use
Used for:
- Client-server communication  
- Network programming  
- Receiving data from remote servers  
- Distributed applications  

## When to Use
Use when:
- A client needs to communicate with a server  
- Data must be received over a network  
- Building TCP-based applications  

Avoid when:
- No network communication is required  
- Local processing is sufficient  

## How to Use
1. Create a socket object  
2. Connect to server using `connect()`  
3. Receive data using `recv()`  
4. Close connection using `close()`  
5. Process received data  

## Advantages
- Simple client-server communication  
- Reliable data transfer using TCP  
- Easy to implement  

## Disadvantages
- Requires a running server  
- Network delays may occur  
- Connection errors must be handled  

## One-Line Summary
This TCP socket client connects to a server, receives data, and displays the server response.
