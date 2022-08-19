#REGULAR EXPRESSIONS
import re
#a set of characters "[a-z]" (or) "[A-Z]"
txt="The rain is Spain"
x=re.findall("[a-z]",txt)
y=re.findall("[A-Z]",txt)
print(x)
print(y)
#Signals a special sequence (can also be used to escape special characters)
txt1="That will be 59 dollars"
a=re.findall("\d",txt1)
print(a)
#.Any character (except newline character)
b=re.findall("r..n",txt)
print(b)
#^Starts with
txt2="hello oooo planet"
c=re.findall("^hello",txt2)
print(c)
#$ the string ends with
d=re.findall("planet$",txt2)
print(d)
#.* zero or more characters
f=re.findall("he.*o",txt2)
print(f)
#.+ one or more occurences
g=re.findall("he.+o",txt2)
print(g)
#.? zero or one occurences
txt3="helo python"
r=re.findall("he.?o",txt3)
print(r)
#{} eaxtly the specified number of occurences
t=re.findall("he.{2}o",txt2)
print(t)
#| either or
txt4="The rain in Spain falls mainly in the plain!"
#check if the string contains either "falls" or "stays"
q=re.findall("falls|stays",txt4)
print(q)


