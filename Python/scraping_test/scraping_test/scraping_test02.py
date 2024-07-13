import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0"}
#url="https://syosetu.com/syuppan/view/bookid/3387/"
url="https://syosetu.com/"
response = requests.get(url=url, headers=headers)
soup = BeautifulSoup(response.content, "lxml")
for element in soup.find_all('a'):
    url2 = element.get("href")
    if re.search('https://', url2):
        if not url==url2:
            print(url2)
            #r = requests.get(url)	
            #s = BeautifulSoup(r.content, "html.parser")


