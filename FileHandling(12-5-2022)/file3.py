#writing the data into file
f=open("text.txt",'w')
f.write("sandhya")
f.write("maha")
f.close()
#reading the data
f=open("text.txt",'r')
print(f.read())


