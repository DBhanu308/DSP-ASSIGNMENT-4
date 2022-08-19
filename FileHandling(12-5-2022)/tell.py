#position of the file handle before reading or writing to file
f=open("text2.txt",'r')
print(f.read())#prints index after read the all the content
print(f.tell())
f.close()
