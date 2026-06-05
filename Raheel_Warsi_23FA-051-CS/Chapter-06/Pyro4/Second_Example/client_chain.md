# Pyro4 Chain Topology Client

## Description
This code demonstrates a Pyro4 client that starts a message traversal through a chain of remote objects.

## What This Code Does
- Connects to the first node in the chain topology  
- Sends an initial message list containing `"hello"`  
- Invokes the remote `process()` method  
- Receives the final traversal result  
- Prints the complete chain path  

## Execution Flow
1. Import Pyro4 library  
2. Create proxy for chain node:
   ```python
   PYRONAME:example.chainTopology.1
   ```
3. Send initial message:
   ```python
   ["hello"]
   ```
4. Remote nodes process and forward the message  
5. Final result is returned to the client  
6. Print the returned chain information  

## How to Execute
1. Install Pyro4:
   ```bash
   pip install Pyro4
   ```

2. Start Pyro Name Server:
   ```bash
   python -m Pyro4.naming
   ```

3. Start all chain topology server nodes

4. Run:
   ```bash
   python client.py
   ```

## End Use
Used for:
- Testing chain topology  
- Distributed message routing  
- Remote object communication  
- Network simulation  

## When to Use
Use when:
- A client needs to initiate a chain process  
- Testing distributed workflows  
- Verifying communication between nodes  

Avoid when:
- Direct server communication is sufficient  
- No chain traversal is required  

## How to Use
1. Create proxy to first chain node  
2. Call `process()` method  
3. Pass initial message list  
4. Receive and display final result  

## Advantages
- Simple client implementation  
- Demonstrates distributed communication  
- Easy to test chain topology  

## Disadvantages
- Depends on running server nodes  
- Requires Name Server setup  
- Network failures can interrupt execution  

## One-Line Summary
This Pyro4 client starts a message traversal through a chain of remote objects and displays the final result.
