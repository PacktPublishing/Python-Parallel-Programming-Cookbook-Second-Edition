f = open ('test.txt', 'w')
f.write ('first line of file \n') 

f.write ('second line of file \n') 

f.close()
f = open ('test.txt')
content = f.read()
print (content)

f.close()
