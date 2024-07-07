import requests
import re
from bs4 import BeautifulSoup
import csv
	
url = 'https://www.ikyu.com/area/ma000000/t413/p3/'
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
elems1 = soup.select('.image > img')
elems2 = soup.select('.relative .block > a')
elems3 = soup.select('.ribbonIconbox > span')

with open('test.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    for i, elem in enumerate(elems1):
        num=elems3[i].text
        hotel=elems1[i]['alt']
        print(num)
        print(hotel)
        url2 = "https://www.ikyu.com" + elems2[i]['href']
        print(url2)
        response2 = requests.get(url2)
        soup2 = BeautifulSoup(response2.text, "html.parser")
        #elems3 = soup2.select('.mr-3 > a')
        #print(elems3[0].text)
        elems99= soup2.select('.bg-gray-100 > span')
        basyo=elems99[2].text
        tel=elems99[5].text
        print(basyo)
        print(tel)
        print()
        mylist = [num, hotel,'', basyo,'','', tel,'']
        writer.writerow(mylist)




#print(elems)

#elems2 = soup.select('.caption_left > a')
#print(elems2)
