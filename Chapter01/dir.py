# In this program, 
# we check if the number is positive or
# negative or zero and 
# display an appropriate message

num = 1

# Try these two variations as well:
# num = 0
# num = -4.5

if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")



# Program to find the sum of all numbers stored in a list

# List of numbers
numbers = [6, 6, 3, 8, -3, 2, 5, 44, 12]

# variable to store the sum
sum = 0

# iterate over the list
for val in numbers:
	sum = sum+val

# Output: The sum is 48
print("The sum is", sum)

