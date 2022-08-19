#ELSE CONDITION WITH WHILE BLOCK
i=1
while(i<=5):
    print(i)
    i=i+1
else:
    print("the while loop exhausted")
#EXAMPLE-2
i=1
while(i<=5):
    print(i)
    i=i+1
    if(i==3):
        break
else:
    print("the while loop is exhausted")
    
