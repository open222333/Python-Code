import requests
from bs4 import BeautifulSoup

'''bs4 練習
BeautifulSoup find 的各種用法
http://python-learnnotebook.blogspot.com/2018/01/beautifulsoup-instructions.html
'''

url = 'https://www.w3schools.com/cssref/css_selectors.asp'
text = requests.get(url)
soup = BeautifulSoup(text.text, 'lxml')
# print(soup.prettify())
div = soup.select('div.w3-col.l3.m3.s12 a')
# soup.select('[aria-label="Last Page"]')
url = soup.find('a').get('href')

soup.find_all('h4', 'card-title')
soup.find_all('h4', {'class': 'card-title'})

soup.find_all('h4', class_='card-title')

print(div)
print(url)
