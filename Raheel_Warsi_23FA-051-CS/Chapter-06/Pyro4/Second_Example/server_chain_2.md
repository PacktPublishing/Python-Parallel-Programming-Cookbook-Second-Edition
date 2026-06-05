# Pyro4 Chain Topology Server 2

## Description
This code creates the second server node in a Pyro4 Chain Topology and forwards messages to Server 3.

## What This Code Does
- Creates a chain node with current server `"2"`  
- Sets next server as `"3"`  
- Registers the node as a remote Pyro object  
- Publishes the service in the Pyro Name Server  
- Waits for requests from other chain nodes  
- Forwards messages to the next server in the chain  

## Execution Flow
1. Import Pyro4 and `chainTopology` module  
2. Set:
   - Current server = `"2"`  
   - Next server = `"3"`  
3. Create service name:
   ```python
   example.chainTopology.2
   ```
4. Create Pyro daemon  
5. Create `Chain` object  
6. Register object with daemon  
7. Locate Pyro Name Server  
8. Register object name and URI  
9. Print startup message  
10. Start request loop using `daemon.requestLoop()`  

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
   python server2.py
   ```

4. Ensure Server 1 and Server 3 are also running

5. Run the client application

## End Use
Used for:
- Distributed systems  
- Chain topology communication  
- Message forwarding between nodes  
- Remote procedure calls (RPC)  

## When to Use
Use when:
- Building multi-node communication chains  
- Simulating routing behavior  
- Creating distributed workflows  

Avoid when:
- Direct communication is sufficient  
- No chain forwarding is required  

## How to Use
1. Define current and next server IDs  
2. Create a `Chain` object  
3. Register it with Pyro daemon  
4. Register service in Name Server  
5. Start request loop to handle incoming messages  

## Advantages
- Supports scalable chain topologies  
- Easy node-to-node communication  
- Demonstrates distributed RPC concepts  

## Disadvantages
- Requires multiple running servers  
- Dependent on Name Server  
- Failure of one node affects the chain  

## One-Line Summary
This Pyro4 server represents the second node in a chain topology and forwards messages to Server 3.
