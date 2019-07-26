class Myclass:
    common = 10
    def __init__ (self):
        self.myvariable = 3
    def myfunction (self, arg1, arg2):
        return self.myvariable

instance = Myclass()
print("instance.myfunction(1, 2)" , instance.myfunction(1, 2))

instance2 = Myclass()
print("instance.common ",instance.common)
print("instance2.common ",instance2.common)

Myclass.common = 30

print("instance.common ", instance.common)

print("instance2.common ", instance2.common)

instance.common = 10
print("instance.common ", instance.common)

print("instance2.common " , instance2.common)
Myclass.common = 50

print("instance.common ", instance.common)
print("instance2.common " , instance2.common)

class AnotherClass (Myclass):
    # The "self" argument is passed automatically
    # and refers to the class's instance, so you can set
    # instance variables as above, but from within the class.
    def __init__ (self, arg1):
        self.myvariable = 3
        print (arg1)

instance = AnotherClass ("hello")
print("instance.myfunction (1, 2) " , instance.myfunction (1, 2))

instance.test = 10
print("instance.test " , instance.test)






