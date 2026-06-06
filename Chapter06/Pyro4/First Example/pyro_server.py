# Pyro4 remote object server

import Pyro4


class Server(object):

    # Exposed remote method
    @Pyro4.expose
    def welcomeMessage(self, name):
        return "Hi welcome " + str(name)


def startServer():

    server = Server()

    # Create Pyro daemon
    daemon = Pyro4.Daemon()

    # Locate Pyro name server
    ns = Pyro4.locateNS()

    # Register remote object
    uri = daemon.register(server)

    # Register object name
    ns.register("server", uri)

    print("Ready. Object uri =", uri)

    # Wait for remote requests
    daemon.requestLoop()


if __name__ == "__main__":
    startServer()