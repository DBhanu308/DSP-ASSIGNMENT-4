#STRING OPERATIONS IMMUTABLE
#1.STRING TYPE
str=input("enter the string:")
print("the given string is:",str)
print("the type of given string is:",type(str))
#2.STRING INDEXING AND SPLITTING
print(str[0])
print(str[1])
print(str[2])
#SPLITTING
print(str[0:])
print(str[1:5])
print(str[2:4])
print(str[:3])
print(str[4:7])
print(str[::3])
#INDEXING
print(str[-1])
print(str[-3])
print(str[-2:])
print(str[-4:-1])
print(str[-7:-2])
print(str[::-1])
#REPEATING THE STRING
a=str*4
print(a)
#CONCATENATION
str1=input("enter the string:")
print("the given string is:",str1)
b=str+str1
print("the concatenation string will be:",b)
#CAPITALIZE
str=input("enter the string(to capitalize):")
cap_str=str.capitalize()
print("the capitalize string will be:",cap_str)
#CASEFOLD(CONVERTS ALL CHARACTERS OF THE STRING INTO LOWERCASE )
str=input("enter the string to casefold:")
casefold_str=str.casefold()
print("the casefold string is:",casefold_str)
#COUNT METHOD
str=input("enter the string to count the substring:")
sub_str="h"
a=str.count(sub_str)
print("the no of times the sub string present in the string is:",a)
#ENDS WITH METHOD
a="python is fun"
print(a.endswith("fun"))
#ENCODE METHOD
str=input("enter the string to encode:")
a=str.encode()
print("the encodes strin will be:",a)
#FIND(index of the first occurence of the sub string)
str="python is fun programming language"
print("the substring index position will be:",str.find("fun"))
#INDEX METHOD
print("the substring index position will be:",str.index("fun"))
#ISALNUM METHOD
str=input("enter the string to isalnum:")
a=str.isalnum()
print("the string is isalnum are not:",a)
#ISALPHA
str=input("enter the string to isalpha:")
a=str.isalpha()
print("the string is isalpha are not:",a)
#ISDECIMAL
str=input("enter the string to isalpha:")
a=str.isdecimal()
print("the string is isdecimal are not:",a)
#ISDIGIT
str=input("enter the string for isdigit:")
a=str.isdigit()
print("the string is isdigit are not:",a)
#ISIDENTIFIER METHOD
str=input("enter the string to isidentifier:")
a=str.isidentifier()
print("the string is identifier are not:",a)
#ISLOWER METHOD
str=input("enter the string to islower:")
a=str.islower()
print("the string is islower are not:",a)
#ISNUMERIC METHOD
str=input("enter the string to isnumeric:")
a=str.isnumeric()
print("the string is isnumeric are nor:",a)
#ISPRINTABLE
str=input("enter the string to isprintable:")
a=str.isprintable()
print("the string is printable are not:",a)
#ISPACE()METHOD PRINTS TRUE IF AAL THE CHARACTERS IN THE STRING WILL BE SPACES OTHERWISE FALSE
str=input("enter the string to isspace:")
a=str.isspace()
print("the string is isspace or not:",a)
#ISTITLE METHOD
str=input("enter the string to istitle:")
a=str.istitle()
print("the string is isspace or not:",a)
#ISUPPER()
str=input("enter the string to isupper:")
a=str.isupper()
print("the string is isupeer or not:",a)
#JOIN
text=["python","is","a","fun","programming","language"]
a=" ".join(text)
print("the join string will be:",a)
#RJUST()
string="cat"
width=5
fillchar="*"
print("the rjust string will be:",string.rjust(width,fillchar))
#LJUST()
string="cat"
width=5
fillchar="*"
print("the ljust string will be:",string.ljust(width,fillchar))
#LOWER()
msg="PYTHON IS A PROGRAMMING LANGUSGE"
print("the lower case string will be:",msg.lower())
#UPPER()
msg="python is a programming language"
print("the upper case string will be:",msg.upper())
#SWAPCASE()
str="THIS SHOULD ALL BE swapcae."
print("the swapcase string will be:",str.swapcase())
#LSTRIP()
str="  this is good"
print("the lstrip string will be:",str.lstrip())
#RSTRIP()
str="this is good  "
print("the rstrip string will be:",str.rstrip())
#STRIP()
str="    learn python   "
print("the strip string will be:",str.strip())
#PARTITION
str="python is fun"
print("the partiton string will be:",str.partition("is"))
#REPLACE
text="bat ball"
print("the string after replace is:",text.replace("b","c"))
#RFIND()[returns the highest index of the substring]
str="let it be,let it be,let it be,let it be."
print("the string(rfind):",str.rfind("let it"))
#RINDEX()
print("the string(rindex):",str.rfind("let it"))
#SPLIT
text="python is a fun programming language."
print("the string after slipt is:",text.split(" "))
#RSPLIT
str="love thy neibhor"
print("the string after rstrip is:",str.rstrip())
print(str.rsplit(','))
print(str.rsplit(':'))
#SLPITLINES
grocery="milk\nchicken\nbread\nbutter"
print("the string after splitlines:",grocery.splitlines())
#STARTSWITH
msg="python is fun"
print("the string after startswith is:",msg.startswith("python"))

