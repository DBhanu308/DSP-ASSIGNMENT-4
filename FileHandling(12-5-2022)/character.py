#using for loop read character by character
f=open("text2.txt",'r')
for i in f:
    print(i)
f.close()
#line by line using for
f=open("text2.txt",'r')
for i in f:
    if i!="\n":
        print(i)
        break
f.close()
#all lines by for loop
f=open("text2.txt",'r')
for i in f:
    if i!=" ":
        print(i)
    else:
        print()
f.close()
