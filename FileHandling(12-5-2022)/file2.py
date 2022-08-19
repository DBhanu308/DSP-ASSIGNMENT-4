#writing the data into file
f=open("file.txt",'w')
f.write("sandhya")
f.close()
#reading the data
f=open("file.txt",'r')
print(f.read())


