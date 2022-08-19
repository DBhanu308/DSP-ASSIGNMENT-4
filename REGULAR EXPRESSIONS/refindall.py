#regular expressions
#findall() function
import re
txt="sandhya is working in out of class with her friend"
x=re.findall("z",txt)
a=re.findall("in",txt)
print(x)
print("the in present in the given text is:")
print(a)
#search operation
txt1="the rain is spain"
y=re.search("\s",txt1)
print("the first white spaces at the  index position is:" ,y.start())
d=re.search("ai",txt1)
print("the first given string  at the  index position is:" ,d.start())
c=re.search("ai",txt1)
print(c)
#split() operation
txt2="vaheeda sameera nageena"
z=re.split(" ",txt2)
print(z)
b=re.split(" ",txt2,1)
print(b)
#sub() operation
e=re.sub("ai","6",txt1)
print(e)
#sub with count() operator
f=re.sub("ai","9",txt1,1)
print(f)
#span() operator
g=re.search(r"\bs\w+",txt1)
print(g.span())
#string operator
h=re.search(r"\bs\w+",txt1)
print(h.string)
#group() operator
i=re.search(r"\bs\w+",txt1)
print(i.group())






