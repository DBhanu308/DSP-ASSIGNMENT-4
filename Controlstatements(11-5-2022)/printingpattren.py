#PRINTING THE NUMBER PYRAMID
rows=int(input("enter the no of rows:"))
for i in range(0,rows+1):
    for j in range(0,i):
        print(j+1,end=' ')
    print("\n")
#ANOTHER PROGRAM
rows=int(input("enter the no of rows:"))
n=1
for i in range(0,rows+1):
    n=1
    for j in range(0,i):
        print(n,end=' ')
        n=n+1
    print()
#NUMBER PATTREN
rows=int(input("enter the no of rows:"))
n=1
for i in range(0,rows+1):
    for j in range(0,i):
        print(n,end=' ')
        n=n+1
    print()
#NUMBER PATTREN
rows=int(input("enter the no of rows:"))
n=0
for i in range(0,rows+1):
    for j in range(0,i):
        print(n,end=" ")
    n=n+1
    print()
#CHARACTER PATTREN
rows=int(input("enter the no of rows:"))
n=65
for i in range(0,rows+1):
    n=65
    for j in range(0,i):
        ch=chr(n)
        print(ch,end=" ")
        n=n+1
    print()
#ANOTHER CHARACTER PATTREN
rows=int(input("enter the no of rows:"))
n=64
for i in range(0,rows+1):
    for j in range(0,i):
        ch=chr(n)
        print(ch,end=" ")
    n=n+1
    print()
#INVERTED HALF PYRAMID USING NUMBERS
rows=int(input("enter the no of rows:"))
for i in range(rows,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

        
