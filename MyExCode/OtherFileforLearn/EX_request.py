import requests

# url = 'https://ccl.jkimg02.xyz/imgs/actor/a3/54aaa99092bb0.jpg'
# print(requests.get(url).status_code, type(requests.get(url).status_code))


def get_status_code(img_path) -> int:
    return requests.get(img_path).status_code


url = ''
print(get_status_code(url))
