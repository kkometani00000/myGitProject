import requests
from bs4 import BeautifulSoup
	
r = requests.get("https://news.yahoo.co.jp/")
	
soup = BeautifulSoup(r.content, "html.parser")
	
#ニュース一覧のテキストのみ抽出
print(soup)
print(soup.find("ul", "list"))

