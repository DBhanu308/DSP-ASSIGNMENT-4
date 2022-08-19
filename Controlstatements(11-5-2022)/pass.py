#PASS STATEMENT
list=[1,2,3,4,5]
flag=1
for i in list:
    print("current element:",i,end=" ")
    if(i==3):
        pass
        print("\nwe are in pass block\n")
        flag=1
    if flag==1:
        print("\ncame out of pass\n")
        flag=0
#EXAMPLE-2
str=input("\nenter the string:")
for i in str:
    if(i=="h"):
        pass
    print(i)
#EXAMPLE-3
str=input("enter the string:")
for i in str:
    if(i=="h"):
        pass
        print("this is pass block",i)
    print(i)
