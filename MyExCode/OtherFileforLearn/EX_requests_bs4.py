import requests
from bs4 import BeautifulSoup

'''bs4 練習'''

url = 'https://www.w3schools.com/cssref/css_selectors.asp'
text = requests.get(url)
soup = BeautifulSoup(text.text, 'lxml')
# print(soup.prettify())
div = soup.select('div.w3-col.l3.m3.s12 a')
url = soup.find('a').get('href')
print(div)
print(url)
