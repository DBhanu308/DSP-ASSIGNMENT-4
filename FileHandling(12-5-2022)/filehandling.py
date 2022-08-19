#file handling
file=open("file1.txt",'r')
print(file)
#printing the lines and data in the file1.txt file
#read function
a=file.read()
print(a)
#read(n)
file1=open("file1.txt","r")
b=file1.read(2)
print(b)
#readlines()
c=file1.readlines()
print(c)
d=file1.readlines(2)
print(d)
#opening another file
file2=open("data.txt","r")
print(file2)
str1=file2.read(10)
str2=file2.read(5)
str3=file2.read()
print("output of the first read:")
print(str1)
print("output of the second read:")
print(str2)
print("output of the third read:")
print(str3)
#read() methods
str4=file2.read()
print(str4)#this will be empty
#readlines function
file3=open("data.txt","r")
print(file3)
line1=file3.readline()
line2=file3.readline()
line3=file3.readline(10)
print(line1,end=" ")
print(line2,end=" ")
print(line3)
#using while loop
file4=open("data.txt","r")
str=" "
while str:
    str=file4.readline()
    print(str,end=" ")
file4.close()
#using for loop
file5=open("data.txt","r")
for str in file5:
    print(str,end=" ")
file4.close()
#calculating the size of file with and without blank spaces
file6=open("data.txt","r")
print(file6)
str1=" "
size=0
tsize=0
while str1:
    str1=file6.readline()
    tsize=tsize+len(str1)
    size=size+len(str1.strip())
print("total size:",tsize)
print("size after removing all eol and blank lines:",size)
file6.close()
#readlines()
file7=open("data.txt","r")
print(file7)
contents=file7.readlines()
print(contents)
print("first line is:",contents[0])
print("last line is:",contents[len(contents)-1])
#counting size of files in bytes and no of lines
file8=open("data.txt","r")
str=file8.read()
size=len(str)
print("size of the file in bytes:",size)
file8.close()
#writing into the file
file9=open("student.txt","w")
for i in range(3):
    name=input("enter name to store:")
    file9.write(name)
    file9.write("\n")
file9.close()
print("\ndata saved successfully....")
#append method
file10=open("student.txt","a")
for i in range(3):
    name=input("enter the name:")
    file10.write(name)
    file10.write("\n")
file10.close()
print("\nthe data saved successfully....")
#using writelines()
myfile=open("emp.txt","w")
mylist=[]
for i in range(3):
    name=input("enter the employee name:")
    mylist.append(name+"\n")
myfile.writelines(mylist)
myfile.close()
print("data saved...")
#Writing strings as a record to file
myfile1=open("book.txt","a")
ans="y"
while ans=="y":
    bno=int(input("enter nook number:"))
    bname=input("enter the book name:")
    author=input("enter the author name:")
    price=int(input("enter the price:"))
    brec=str(bno)+" "+bname+" "+author+" "+str(price)+"\n"
    myfile1.write(brec)
    ans=input("add more?")
myfile1.close()

    






