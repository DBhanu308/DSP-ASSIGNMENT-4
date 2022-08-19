#CONTINUE STATEMENT
#EXAMPLE-1
i=0
while(i<10):
    i=i+1
    if(i==5):
        continue
    print(i)
#EXAMPLE-2
str=input("enter the string:")
for i in str:
    if(i=="v"):
        continue
    print(i)
