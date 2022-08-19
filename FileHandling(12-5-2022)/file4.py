#write
f=open("file.txt",'w')
f.write("helle hai")
f.close()
#append
f=open("file.txt",'a')
f.write("welcome to python file operations")
f.close()
f=open("file.txt",'r')
print(f.read())
