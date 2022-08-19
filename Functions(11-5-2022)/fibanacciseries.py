#PROGRAM TO PRINT FIBANACCI NUMBERS TO GIVEN LIMIT
terms=int(input("enter the no of terms:"))
a=0
b=1
c=0
count=0
if(terms<=0):
    print("please enter a valid integer.")
elif(terms==1):
    print("fibanacci sequence upto limit.")
    print(a)
else:
    print("fibanacci sequence:")
    while(count<=terms):
        print(c,end=" ")
        c=a+b
        a=b
        b=c
    count=count+1
