# Demonstrates classes, objects, inheritance,
# instance variables, and class variables

class Myclass:
    # Class variable shared by all objects
    common = 10

    def __init__(self):
        # Instance variable
        self.myvariable = 3

    def myfunction(self, arg1, arg2):
        return self.myvariable


# Create object
instance = Myclass()
print("instance.myfunction(1, 2)", instance.myfunction(1, 2))

# Create another object
instance2 = Myclass()

print("instance.common", instance.common)
print("instance2.common", instance2.common)

# Modify class variable
Myclass.common = 30

print("instance.common", instance.common)
print("instance2.common", instance2.common)

# Create instance-specific variable
instance.common = 10

print("instance.common", instance.common)
print("instance2.common", instance2.common)

# Modify class variable again
Myclass.common = 50

print("instance.common", instance.common)
print("instance2.common", instance2.common)


# Child class inheriting from Myclass
class AnotherClass(Myclass):

    def __init__(self, arg1):
        self.myvariable = 3
        print(arg1)


# Create inherited object
instance = AnotherClass("hello")

print("instance.myfunction(1, 2)", instance.myfunction(1, 2))

# Dynamically add an attribute
instance.test = 10

print("instance.test", instance.test)