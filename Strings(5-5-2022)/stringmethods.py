#STRING OPERATIONS
#1.CREATING THE STING
str=input("enter the string:")
print("the entered string is:",str)
#2.ACCESSING THE CHARACTERS N THE STRING
print('str[0]=',str[0])
print('str[-1]=',str[-1])
print('str[1:5]=',str[1:5])
print('str[5:-2]=',str[5:-2])
#STRING CONCATANATION
str1=input("enter the string 1:")
print("the entered second string is:",str1)
str2=str+str1
print("the concatenation string will be:",str2)
#REPEATING THE NUMBER OF STRING
str3=str1*4
print("the no of string is:",str3)
#MEMBERSHIP METHOD
a="hee" in str
print(a)

