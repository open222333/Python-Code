import requests

url = 'https://ccl.jkimg02.xyz/imgs/actor/a3/54aaa99092bb0.jpg'
print(requests.get(url).status_code, type(requests.get(url).status_code))
