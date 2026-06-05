# Pyro4 Chain Topology Server 3

## Description
This code creates the third server node in a Pyro4 Chain Topology and forwards messages back to Server 1, completing the chain.

## What This Code Does
- Creates a chain node with current server `"3"`  
- Sets next server as `"1"`  
- Registers the node as a remote Pyro object  
- Publishes the service in the Pyro Name Server  
- Waits for incoming requests  
- Forwards messages back to Server 1 to complete the topology loop  

## Execution Flow
1. Import Pyro4 and `chainTopology` module  
2. Set:
   - Current server = `"3"`  
   - Next server = `"1"`  
3. Create service name:
   ```python
   example.chainTopology.3
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
   python server3.py
   ```

4. Ensure Server 1 and Server 2 are also running

5. Run the client application

## End Use
Used for:
- Distributed systems  
- Ring/chain topology implementation  
- Message routing simulation  
- Remote procedure calls (RPC)  

## When to Use
Use when:
- Building cyclic communication topologies  
- Simulating network routing paths  
- Testing distributed workflows  

Avoid when:
- Direct communication is sufficient  
- No multi-node communication is needed  

## How to Use
1. Define current and next server IDs  
2. Create a `Chain` object  
3. Register object with Pyro daemon  
4. Register service in Name Server  
5. Start request loop to handle requests  

## Advantages
- Completes the chain topology loop  
- Supports distributed message routing  
- Demonstrates RPC communication across nodes  

## Disadvantages
- Requires all chain nodes to be active  
- Dependent on Name Server availability  
- Failure of one server can break the chain  

## One-Line Summary
This Pyro4 server acts as the third node in the chain topology and forwards messages back to Server 1, completing the communication loop.
