# Demonstrates file writing and reading

# Open file in write mode
f = open('test.txt', 'w')

# Write content to file
f.write('first line of file\n')
f.write('second line of file\n')

# Close file after writing
f.close()

# Open file in read mode
f = open('test.txt')

# Read complete file content
content = f.read()

print(content)

# Close file after reading
f.close()