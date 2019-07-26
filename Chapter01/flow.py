
# IF

# In this program, we check if the number is positive or negative or zero and 
# display an appropriate message

num = 1
if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")


# FOR
# Program to find the sum of all numbers stored in a list
numbers = [6, 6, 3, 8, -3, 2, 5, 44, 12]
sum = 0
for val in numbers:
	sum = sum+val

# Output: The sum is 48
print("The sum is", sum)


#WHILE
# Program to add natural numbers upto sum = 1+2+3+...+n

n = 10
# initialize sum and counter
sum = 0
i = 1
while i <= n:
    sum = sum + i
    i = i+1    # update counter

# print the sum
print("The sum is", sum)

