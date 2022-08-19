#SPECIAL SEQUENCES
#\A Returns the match if the specified characters are at the beginnig of the string
import re
txt="The rain is Spain"
a=re.findall("\AThe",txt)
print(a)
if a:
    print("yes there is match")
else:
    print("no match")
#\b Returns a match where the specified characters are at the beginninng or at the end of a word
b=re.findall(r"\bain",txt)
print(b)
c=re.findall(r"ain\b",txt)
print(c)
#\B Returns a match where the specified characters are present,but not at the beginning
d=re.findall("\Bain",txt)
print(d)
e=re.findall("ain\B",txt)
print(e)
#\d Returns the string contains any digits
txt1="the rain is spain 59"
f=re.findall("\d",txt1)
print(f)
#\D returns a match where the string does not contain digits
g=re.findall("\D",txt)
print(g)
#\s Returns a match where the string contains a white space characters
h=re.findall("\s",txt)
print(h)
#\S Returns a match where the string does not contains a white space characters
txt2="vaheedasameeranageena59_"
i=re.findall("\S",txt2)
print(i)
#\w Returns a match where the string contains any word characters(any word numbers special symbols alse it prints)
j=re.findall("\w",txt2)
print(j)
#\W Returns a match where the string DOES NOT conatain any word characters(characters not between a and Z.like "!","?","white spaces.
k=re.findall("\W",txt2)
print(k)
l=re.findall("\W",txt)
print(l)
#\Z Reurns a match if the specified characters are at the end of the string
m=re.findall("Spain\Z",txt)
print(m)

