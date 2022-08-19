#BREAK STATEMENTS EXAMPLES
#EXAMPLE-1
list=[1,2,3,4,5]
for i in range(len(list)):
    if(list[i]==4):
        continue
    print(list[i])
#EXAMPLE-1
str=input("enter the string:")
for i in str:
    if i=="o":
        break
    print(i)
#EXAMPLE-3
i=0
while 1:
    print(i,end=" ")
    i=i+1
    if(i==10):
        break
print("come our of while loop.")
#EXAMPLE-3
n=int(input("enter the table no:"))
while 1:
    i=1
    while i<=10:
        print(n,"X",i,"=",n*i)
        i=i+1
