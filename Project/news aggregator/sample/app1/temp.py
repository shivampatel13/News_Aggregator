import requests

"""
page = requests.get("https://www.divyabhaskar.co.in/local/gujarat/")
#print(page)
#print(page.content)

from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content,'html.parser')

#print(soup.prettify())
#print(list(soup.children))

d=soup.find_all("div")

#print(d)

l1=[]
for i in d:
    #print(i)
    p=i.find("h3")
    if p is not None:
        #print(p.text.strip())
        l1.append(p.text.strip())


print(l1)
print(len(l1))
s=set(l1)
print(len(s))

s=list(s)
print(len(s))
for i in s:
    print(i)


h=soup.find_all("img")
for i in h:
    #print(i)
    print(i.get('src'))
"""
page = requests.get("https://www.gujaratsamachar.com/city/baroda/1")
from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content,'html.parser')
print(list(soup.children))

d=soup.find_all("div")

#print(d)

l1=[]
for i in d:
    print(i)
    p=i.find("h2")
    #div_elem = i.find('div')
    if p is not None:
        print(p.text.strip())
        #l1.append(p.text.strip())