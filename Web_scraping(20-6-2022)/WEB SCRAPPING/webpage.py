#web scrapping
import urllib.request
import re
url="https://www.w3schools.com/"
page=urllib.request.urlopen(url)
print(page)
html_bytes=page.read()
html=html_bytes.decode("utf-8")#for the html we use "utf-8"
print(html)
title_index=html.find("<title>")
print(title_index)
start_index=title_index+len("<title>")
print(start_index)
end_index=html.find("</title>")
print(end_index)
title=html[start_index:end_index]
print(title)
#for only one link
anchor=html.find("<a")
print(anchor)
closing=html.find("</a>")
print(closing)
link=html[anchor:closing]
print(link)
#finding the anchor tags
anchor_tag=re.findall("<a",html)
print(anchor_tag)
length_anchor_tag=len(anchor_tag)
print(length_anchor_tag)
#print the headings
headings=re.findall(r"<h[1-6]>(.+)</h[1-6]>",html)
print(headings)
links_name=re.findall(r"<a href=.+>(.+)</a>",html)
print(links_name)
links=re.findall(r"<a href=(.+)>.+</a>",html)
print(links)
image=re.findall(r"<img src=(.+)>",html)
print(image)
paragraph=re.findall(r"<p>(.+)</p>",html)
print(paragraph)

