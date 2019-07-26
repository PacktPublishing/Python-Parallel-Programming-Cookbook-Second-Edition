from __future__ import print_function
import Pyro4


# a Chain member. Passes messages to the next link,
# until the message went full-circle: then it exits.
@Pyro4.expose
class Chain(object):
    def __init__(self, name, next):
        self.name = name
        self.nextName = next
        self.next = None
    
    def process(self, message):
        if self.next is None:
            self.next = Pyro4.core.Proxy("PYRONAME:example.chainTopology." + self.nextName)
        if self.name in message:
            print("Back at %s; the chain is closed!" % self.name)
            return ["complete at " + self.name]
        else:
            print("%s forwarding the message to the object %s" % (self.name, self.nextName))
            message.append(self.name)
            result = self.next.process(message)
            result.insert(0, "passed on from " + self.name)
            return result
