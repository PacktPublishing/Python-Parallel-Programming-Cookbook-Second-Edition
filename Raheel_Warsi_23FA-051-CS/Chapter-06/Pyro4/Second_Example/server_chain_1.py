import Pyro4
import chainTopology

current_server = "1"
next_server = "2"

servername = "example.chainTopology." + current_server

daemon = Pyro4.core.Daemon()
obj = chainTopology.Chain(current_server, next_server)
uri = daemon.register(obj)
ns = Pyro4.locateNS()
ns.register(servername, uri)

# enter the service loop.

print("server_%s started " % current_server)
daemon.requestLoop()
