**Chapter 06 — Distributed Computing**

This chapter covers how to make programs communicate across a network — from basic socket connections to task queues and remote object calls. Three technologies are explored: Sockets, Celery, and Pyro4.


**socket/server.py — Simple Time Server**
Opens a socket on port 9999, waits for a client to connect, then sends back the current time.
Loops forever, handling one client at a time.


**socket/client.py — Simple Time Client**
Connects to the server on port 9999 and receives the current time string.
Prints it and closes the connection.


**socket/server2.py — File Transfer Server**
Listens for a client connection, then reads mytext.txt and sends its contents over the socket.
After sending, closes the connection with a thank-you message.


**socket/client2.py — File Transfer Client**
Connects to server2.py, receives the file data, and saves it to received.txt.
Keeps receiving until the server stops sending, then closes the connection.


**Celery/addTask.py — Define a Background Task**
Creates a Celery app connected to a RabbitMQ broker and defines an add(x, y) task.
The @app.task decorator registers it so Celery workers can pick it up and run it.


**Celery/addTask_main.py — Trigger the Task Asynchronously**
Calls add.delay(5, 5) to send the task to the queue without waiting for the result.
The actual addition runs in a separate Celery worker process in the background.


**Pyro4/First Example/pyro_server.py — Remote Object Server**
Registers a Server object with Pyro4's name server so it can be called remotely.
Exposes a welcomeMessage(name) method that clients can call as if it were local.


**Pyro4/First Example/pyro_client.py — Remote Object Client**
Looks up the Server object by name and calls welcomeMessage() on it remotely.
Pyro4 handles all the networking — the call looks like a normal Python method call.


**Pyro4/Second Example/chainTopology.py — Chain of Remote Objects**
Defines a Chain object that forwards a message to the next server in a chain.
The message hops from server to server until it loops back to the start.


**Pyro4/Second Example/client_chain.py — Start the Chain**
Connects to the first server in the chain and sends a message to kick it off.
Prints the full result once the message has travelled through all the servers.


**Pyro4/Second Example/server_chain_1/2/3.py — Chain Nodes**
Each file registers one Chain node (linked to the next) with the Pyro4 name server.
Together, they form the three-link chain that passes messages between them.


**Technologies at a Glance**

socket — Low-level network communication between two machines
Celery — Distributes tasks to background workers via a message broker
Pyro4 — Call Python objects on remote machines like local functions
