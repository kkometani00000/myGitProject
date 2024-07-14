import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0"}
#url="https://syosetu.com/syuppan/view/bookid/3387/"
url="https://syosetu.com/"
response = requests.get(url=url, headers=headers)
html = response.content
soup = BeautifulSoup(html, "lxml")
all_text=soup.find_all('a')
for element in all_text:
    url = element.get("href")
    if re.search('https://', url):
        print(url)