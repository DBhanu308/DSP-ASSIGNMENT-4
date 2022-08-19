#finding the gmail accounts ina given text
import re
txt="Hello from shaikvaheeda252@gmail.com to s180252@rguktsklm.ac.in and priys@yahoo.com about the meeting @2PM."
a=re.findall("\S+@\S+",txt)
print(a)
c=re.findall("[a-zA-Z0-9]\S*@\S*[a-zA-Z0-9]",txt)
print(c)
#another
my_text = "Please contact us at contact@tutorialspoint.com for further information.+\ You can also give feedback at feedback@tutorialspoint.com"
b=re.findall("[a-zA-Z0-9]\S*@\S*[a-zA-Z0-9]",my_text)
print(b)
my_text = "Please contact us at contact@tutorialspoint.com for further information."+\
   " You can also give feedback at feedback@tutorialspoint.com"
my_emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", my_text)
print (my_emails)

