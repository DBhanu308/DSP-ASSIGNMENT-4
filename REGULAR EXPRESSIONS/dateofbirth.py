#finding the date of birth
import re
s="vaheeda 2003-09-15, sameera 2006-01-06 nageena 2000-08-31"
match=re.findall(r"\d{4}-\d{2}-\d{2}",s)
print("the date of births in the given text are:",match)
#another way
import datetime
from datetime import date
import re
s = "Jason's birthday is on 1991-09-21,2006-09-31"
match = re.search(r'\d{4}-\d{2}-\d{2}', s)
date = datetime.datetime.strptime(match.group(), '%Y-%m-%d').date()
print(date)
#extract floating
txt="sound levle:-117.7 db or 15.2 or 8 db"
a=re.findall(r"[-+]?\d*\.\d+|\d+",txt)
print(a)
#extracting the time
txt2= 'Mon - Fri:,10:00 am - 7:00 pm'
r=re.findall(r"\s\d{2}:\d{2}\s""[a-zA-Z]",txt2)
print(r)
data = re.findall(r'\s(\d{2}\:\d{2}\s?(?:AM|PM|am|pm))', txt2)
print(data)
d=re.findall(r"\b([01]?[0-9]|2[0-3]):([0-5][0-9])(?::([0-9][0-9]))?\b",txt2)
print(d)
