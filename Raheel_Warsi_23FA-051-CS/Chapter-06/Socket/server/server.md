# TCP Socket Time Server

## Description
This code demonstrates a simple TCP server that sends the current system time to connected clients.

## What This Code Does
- Creates a TCP server socket  
- Binds the server to port `9999`  
- Listens for incoming client connections  
- Accepts client requests continuously  
- Sends the current date and time to the client  
- Closes the client connection after sending data  

## Execution Flow
1. Create a TCP socket  
2. Get local machine hostname  
3. Bind socket to port `9999`  
4. Start listening for connections using `listen(5)`  
5. Wait for a client connection using `accept()`  
6. Get current system time  
7. Send time to the client  
8. Close client connection  
9. Continue waiting for new clients  

## How to Execute
1. Open terminal in this folder  
2. Run:
   ```bash
   python server.py
   ```
3. Run the client program in another terminal

## End Use
Used for:
- Client-server communication  
- Network programming practice  
- Time synchronization services  
- TCP server implementation learning  

## When to Use
Use when:
- Multiple clients need information from a server  
- Building network-based applications  
- Learning socket programming  

Avoid when:
- No network communication is required  
- Local execution is sufficient  

## How to Use
1. Create server socket  
2. Bind using `bind()`  
3. Start listening using `listen()`  
4. Accept connections using `accept()`  
5. Send data using `send()`  
6. Close client connection after processing  

## Advantages
- Simple TCP server implementation  
- Supports multiple client connections  
- Reliable communication using TCP  

## Disadvantages
- Handles clients sequentially  
- No concurrency support  
- Limited error handling  

## One-Line Summary
This TCP socket server waits for client connections and sends the current system time to each connected client.
