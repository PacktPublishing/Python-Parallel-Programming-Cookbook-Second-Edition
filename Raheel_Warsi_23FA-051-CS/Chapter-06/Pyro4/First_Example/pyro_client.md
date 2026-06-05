# Pyro4 Client Application

## Description
This code demonstrates a Pyro4 client that connects to a remote server and invokes a method remotely.

## What This Code Does
- Takes user input (name)  
- Connects to a Pyro4 server using a Name Server  
- Creates a remote object proxy  
- Calls the server method `welcomeMessage()`  
- Displays the response received from the server  

## Execution Flow
1. Import `Pyro4`  
2. Ask user to enter a name  
3. Connect to remote server using:
   ```python
   Pyro4.Proxy("PYRONAME:server")
   ```
4. Call remote method:
   ```python
   server.welcomeMessage(name)
   ```
5. Receive response from server  
6. Print the returned message  

## How to Execute
1. Install Pyro4:
   ```bash
   pip install Pyro4
   ```

2. Start Pyro Name Server:
   ```bash
   python -m Pyro4.naming
   ```

3. Start the Pyro4 server

4. Run:
   ```bash
   python client.py
   ```

## End Use
Used for:
- Remote Procedure Calls (RPC)  
- Distributed applications  
- Client-server communication  

## When to Use
Use when:
- Functions need to be executed on a remote machine  
- Building distributed systems  
- Client-server architecture is required  

Avoid when:
- Local execution is sufficient  
- Network communication is unnecessary  

## How to Use
1. Start Pyro Name Server  
2. Register server object  
3. Create client proxy using server name  
4. Call remote methods like local functions  

## Advantages
- Simple remote method calls  
- Easy distributed application development  
- Object-oriented communication  

## Disadvantages
- Requires network connectivity  
- Additional setup for Name Server  
- Communication overhead  

## One-Line Summary
This Pyro4 client connects to a remote server and executes a method using Remote Procedure Calls (RPC).
