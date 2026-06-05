# Pyro4 Chain Topology

## Description
This code demonstrates a Chain Topology using Pyro4, where remote objects forward messages to each other in sequence until the chain is completed.

## What This Code Does
- Defines a remote `Chain` object  
- Connects to another remote server in the chain  
- Receives and forwards messages between servers  
- Tracks visited servers using a message list  
- Detects when the chain returns to the starting server  
- Returns the complete traversal path  

## Execution Flow
1. Create a `Chain` object with:
   - Server name  
   - Next server name  
2. Receive a message list  
3. Connect to the next server using Pyro4 Proxy  
4. Check if current server already exists in message:
   - If yes, chain is complete  
   - If no, continue forwarding  
5. Add current server name to message list  
6. Forward message to next server  
7. Return results through the chain  

## How to Execute
1. Install Pyro4:
   ```bash
   pip install Pyro4
   ```

2. Start Pyro Name Server:
   ```bash
   python -m Pyro4.naming
   ```

3. Start all chain topology servers

4. Run the client application:
   ```bash
   python client.py
   ```

## End Use
Used for:
- Distributed systems  
- Message routing  
- Network topology simulations  
- Remote object communication  

## When to Use
Use when:
- Messages must pass through multiple servers  
- Distributed workflows are required  
- Network routing behavior is being simulated  

Avoid when:
- Direct client-server communication is sufficient  
- No forwarding logic is needed  

## How to Use
1. Create multiple `Chain` objects  
2. Register each object with Pyro Name Server  
3. Define next server for each node  
4. Send a message to the first node  
5. Allow automatic forwarding through the chain  

## Advantages
- Demonstrates distributed message routing  
- Easy to extend with more nodes  
- Useful for topology simulations  

## Disadvantages
- Network dependency  
- More complex than direct communication  
- Failure of one node can break the chain  

## One-Line Summary
This Pyro4 chain topology forwards messages through multiple remote objects until the chain returns to the starting node.
