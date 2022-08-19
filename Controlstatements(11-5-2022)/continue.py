#WHILE LOOP AND CONTINUE STATEMENT
i=0
str=input("enter the string:")
while i<len(str):
    if str[i]=="a" or str[i]=="t":
        i=i+1
        continue
    print("current letter:",str[i])
    i=i+1
#BREAK STATEMENT
i=0
str=input("enter the string:")
while i<len(str):
    if str[i]=="t":
        i=i+1
        break
    print("current letter:",str[i])
    i=i+1
#PASS STATEMENT
i=0
str=input("enter the string:")
while i<len(str):
    i=i+1
    pass
print("the value of i=",i)
