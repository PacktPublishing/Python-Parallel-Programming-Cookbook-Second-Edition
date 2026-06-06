# Demonstrates Python data structures

# Nested list example
example = [1, ["another", "list"], ("a", "tuple")]

# List operations
mylist = ["element 1", 2, 3.14]

mylist[0] = "yet element 1"
print(mylist[0])

mylist[-1] = 3.15
print(mylist[-1])

# Dictionary operations
mydict = {
    "Key 1": "value 1",
    2: 3,
    "pi": 3.14
}

print(mydict)

mydict["pi"] = 3.15
print(mydict["pi"])

# Tuple example
mytuple = (1, 2, 3)
print(mytuple)

# Store function reference and call it
myfunc = len
print(myfunc(mylist))