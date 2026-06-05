# TCP Socket File Transfer Client

## Description
This code demonstrates a TCP client that connects to a server, receives a file, and saves it locally.

## What This Code Does
- Creates a socket connection to a server  
- Sends a request message (`HelloServer!`)  
- Receives file data from the server  
- Stores received data in `received.txt`  
- Closes the connection after file transfer is complete  

## Execution Flow
1. Create a socket object  
2. Connect to server on port `60000`  
3. Send greeting message:
   ```python
   HelloServer!
   ```
4. Open `received.txt` in write-binary mode  
5. Receive data in chunks of 1024 bytes  
6. Write received data into the file  
7. Stop when no more data is received  
8. Close file and socket connection  

## How to Execute
1. Start the file server first  
2. Open terminal in this folder  
3. Run:
   ```bash
   python client.py
   ```

## End Use
Used for:
- File transfer applications  
- Client-server communication  
- Downloading files from servers  
- Network-based file sharing  

## When to Use
Use when:
- Files need to be transferred over a network  
- A client must download data from a server  
- Building file-sharing applications  

Avoid when:
- No file transfer is required  
- Local file access is sufficient  

## How to Use
1. Create a socket connection  
2. Send request to server  
3. Open destination file  
4. Receive data using `recv()`  
5. Write data to file  
6. Close file and connection  

## Advantages
- Simple file transfer implementation  
- Reliable TCP communication  
- Can handle large files in chunks  

## Disadvantages
- Requires active server connection  
- No error handling for failed transfers  
- Transfer speed depends on network performance  

## One-Line Summary
This TCP socket client downloads a file from a server and saves it locally as `received.txt`.
