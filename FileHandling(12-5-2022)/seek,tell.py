#tell function
myfile2=open("student.txt")
print(myfile2)
print(myfile2.tell())
print(myfile2.seek(0))
#strip method
file=open("ipl.txt","r")
print(file)
line1=file.readline()
print("the length of the line1 is:",len(line1))
line1=line1.rstrip()
print("the length of the line1 is:",len(line1))
line2=file.readline()
print(line2)
print("the length of the line2 is:",len(line2))
line2=line2.lstrip()
print(line2)
print("the length of the line2 is:",len(line2))
#copy the one file content to another file
file1=open("BOOK1.txt","r")
file2=open("book2.txt","w")
print(file1)
print(file2)
str=" "
while str:
    str=file1.readline()
    file2.write(str)
file1.close()
file2.close()
print("the data is successfully copied:")
#read the content of the text file
file5=open("ipl.txt","r")
print(file5)
print(file5.read(5))
print(file5.read(8))
file5.close()
#using flush function
file4=open("temp.txt","w+")
print(file4)
file4.write("hello ")
file4.write("hii sister ")
file4.flush()#here without flish function are also it will executed
n=input("press any key:")
file4.write("go to home")
file4.close()
#using with function
with open("newfile.txt","w") as mf:
    mf.write("vaheeda ")
    mf.write("sameera")
print(mf)





