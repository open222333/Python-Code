import requests

html = requests.get('https://www.studyusa.com/zh-tw/schools/p/ms004/university-of-mississippi')
print(html.text)