# Pyro4 remote object client

import Pyro4

# Get user input
name = input("What is your name? ").strip()

# Connect to remote object
server = Pyro4.Proxy("PYRONAME:server")

# Invoke remote method
print(server.welcomeMessage(name))