import requests
import re
from bs4 import BeautifulSoup
	
url = 'https://news.yahoo.co.jp'
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
elems = soup.find_all(href=re.compile("news.yahoo.co.jp/pickup"))
#print(elems)
#print()
#print()

for elem in elems:
    print(elem.contents[0])
    print(elem.attrs['href'])
    #print(elem.contents[0] + ": " + elem.attrs['href'])
