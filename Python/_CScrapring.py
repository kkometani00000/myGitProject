import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0"}

class Scrapring():
    def __init__(self, url):
        self.__url = url

    def get_data(self):
        response = requests.get(url=self.__url, headers=headers)
        soup = BeautifulSoup(response.content, "lxml")
        for element in soup.find_all('a'):
            url2 = element.get("href")
            if re.search('https://', url2):
                if not self.__url==url2:
                    print(url2)
        return self.__url

