# TCP Socket File Transfer Server

## Description
This code demonstrates a TCP server that sends a file to a connected client.

## What This Code Does
- Creates a TCP server socket  
- Waits for client connections on port `60000`  
- Receives a request from the client  
- Opens `mytext.txt` file  
- Sends file contents to the client in chunks  
- Sends a final thank-you message  
- Closes the connection  

## Execution Flow
1. Create a socket object  
2. Bind socket to port `60000`  
3. Start listening for client requests  
4. Accept a client connection  
5. Receive client message  
6. Open `mytext.txt` in binary mode  
7. Read file data in chunks of 1024 bytes  
8. Send file data to client using `send()`  
9. Send completion message  
10. Close client connection  

## How to Execute
1. Place `mytext.txt` in the same folder  
2. Open terminal in this folder  
3. Run:
   ```bash
   python server.py
   ```
4. Run the client program from another terminal

## End Use
Used for:
- File transfer systems  
- Client-server communication  
- Network file sharing  
- Data distribution over TCP  

## When to Use
Use when:
- Files need to be shared across a network  
- A server must send data to clients  
- Building file transfer applications  

Avoid when:
- File sharing is not required  
- Local file access is sufficient  

## How to Use
1. Create server socket  
2. Bind to a port  
3. Listen for incoming clients  
4. Open file in binary mode  
5. Send file contents using `send()`  
6. Close connection after transfer  

## Advantages
- Simple file transfer implementation  
- Reliable data delivery with TCP  
- Supports large file transfer in chunks  

## Disadvantages
- Handles one client at a time  
- Limited error handling  
- No encryption or security features  

## One-Line Summary
This TCP socket server sends the contents of a file to connected clients over a TCP connection.
