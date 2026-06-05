# Pyro4 Server Application

## Description
This code demonstrates a Pyro4 server that exposes a remote method and waits for client requests.

## What This Code Does
- Creates a server class with a remote method  
- Exposes `welcomeMessage()` for remote access  
- Starts a Pyro daemon  
- Registers the server with the Pyro Name Server  
- Waits for incoming client requests  
- Returns a welcome message to connected clients  

## Execution Flow
1. Create `Server` class  
2. Define remote method `welcomeMessage()`  
3. Create Pyro daemon  
4. Locate Pyro Name Server  
5. Register server object with daemon  
6. Register object name (`server`) in Name Server  
7. Display generated URI  
8. Start request loop and wait for client calls  

## How to Execute
1. Install Pyro4:
   ```bash
   pip install Pyro4
   ```

2. Start Pyro Name Server:
   ```bash
   python -m Pyro4.naming
   ```

3. Run the server:
   ```bash
   python server.py
   ```

4. Run the client program in another terminal

## End Use
Used for:
- Remote Procedure Calls (RPC)  
- Distributed systems  
- Client-server applications  
- Remote object communication  

## When to Use
Use when:
- Remote method execution is needed  
- Building distributed applications  
- Multiple clients need access to shared services  

Avoid when:
- Local execution is sufficient  
- Network communication is unnecessary  

## How to Use
1. Create server class  
2. Expose methods using `@Pyro4.expose`  
3. Register object with daemon  
4. Register object name with Name Server  
5. Start request loop using `requestLoop()`  
6. Connect through a Pyro4 client  

## Advantages
- Simple RPC implementation  
- Object-oriented communication  
- Easy client-server development  

## Disadvantages
- Requires Name Server setup  
- Network dependency  
- Additional communication overhead  

## One-Line Summary
This Pyro4 server exposes a remote method that clients can call over a network using RPC.
