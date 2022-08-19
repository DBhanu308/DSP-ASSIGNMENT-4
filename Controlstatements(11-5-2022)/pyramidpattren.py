#PROGRAM TO PRINT FULL PYRAMID USING *
rows=int(input("enter the no of rows:"))
k=0
for i in range (1,rows+1):
    for space in range(1,(rows-i)+1):
        print(" ",end=" ")
    while k!=(2*i-1):
        print("*",end=" ")
        k=k+1
    k=0
    print()
#DISPLAY LETTER OF THE WORD IN PATTERN
str=input("enter the string:")
x=""
for i in str:
    x=x+i
    print(x)
#RIGHT-ANGLED PATTREN WITH SAME CHARACTER
rows=int(input("enter the no of rows:"))
asciivalue=int(input("enter the asciivalues of the character:"))
if(asciivalue>=65 and asciivalue<=122):
    for i in range(0,rows+1):
        for j in range (0,i):
            alpha=chr(asciivalue)
            print(alpha,end=" ")
        print()
else:
    print("enter the valid character ascii value.")
#RIGHT-ANGLED INVETED PATTREN WITH SAME CHARACTER
rows=int(input("enter the no of rows:"))
asciivalue=int(input("enter the asciivalues of the character:"))
if(asciivalue>=65 and asciivalue<=122):
    for i in range(rows,0,-1):
        for j in range (0,i):
            alpha=chr(asciivalue)
            print(alpha,end=" ")
        print()
else:
    print("enter the valid character ascii value.")
#MULTIPLICATION NUMBER IN COLUMN
rows=int(input("enter the no of rows:"))
for i in range(1,rows+1):
    for j in range(1,i+1):
        print(i*j,end=" ")
    print()
#MULTIPLICATION NUMBER IN COLUMN
rows=int(input("enter the no of rows:"))
for i in range(rows,1,-1):
    for j in range(1,i+1):
        print(i*j,end=" ")
    print()    
#SQUARE PATTREN USING WITH NUMBERS
rows=int(input("enter the no of rows:"))
for i in range(1,rows+1):
    for j in range(1,rows+1):
        if j<=i:
            print(i,end=" ")
        else:
            print(j,end=" ")
    print()
#SQUARE PATTREN USING WITH NUMBERS
rows=int(input("enter the no of rows:"))
for i in range(rows+1,1,-1):
    for j in range(1,rows+1):
        if j<=i:
            print(i,end=" ")
        else:
            print(j,end=" ")
    print()
#PYRAMID PATTREN
rows=int(input("enter the no of rows:"))
k=0
for i in range(1,rows+1):
    k=k+1
    for j in range(1,i+1):
        print(k,end=" ")
    print()
#INVERTED PYRAMID PATTREN
rows=int(input("enter the no of rows:"))
k=rows
for i in range(rows,1,-1):
    k=k-1
    for j in range(0,i):
        print(k,end=" ")
    print()

