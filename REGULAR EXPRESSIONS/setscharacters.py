#SETS Aset is set of characters inside a pair of square brackets[] with special meaning:
import re
#1)[arn] #returns a match where one of the specified characters(a,r,n) is present
txt="The rain is Spain"
a=re.findall("[earn]",txt)
print(a)
#2)[a-n] #returns a match for any lower case charcater,alphabetically between a and n
b=re.findall("[a-z]",txt)
print(b)
c=re.findall("[A-Z]",txt)
print(c)
#3)[^arn] Returns a match for any character EXCEPT a,r,and n
d=re.findall("[^arn]",txt)
print(d)
#4)[0-9] returns a match for any digit between 0 and 9
txt1="8 times before 11:45 AM"
e=re.findall("[0-9]",txt1)
print(e)
#5)[0-5][0-9] Returns a match for any teo-digit numbers from 00 and 59
f=re.findall("[0-5][0-9]",txt1)
print(f)
#6)[01234] Returns a match if the specified digits (0,1,2,3,4)are present
g=re.findall("[0123458]",txt1)
print(g)
#7) [a-zA-Z] Returns a match for any character alphabetically between a and z,lower case OR upper case
h=re.findall("[a-zA-Z]",txt1)
print(h)
#8) [+] In sets,+,-,*,/,.,(),$,{} has no special meaning,so [+] means:return a match for any + character in the string.
txt2="vaheeda +"
i=re.findall("[+]",txt2)
print(i)

