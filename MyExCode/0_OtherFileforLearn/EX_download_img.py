import os
import requests
from bs4 import BeautifulSoup


def get_img_list(urls, class_id=None):
    '''取得圖片列表'''
    img_lists = []
    for url in urls:
        data = requests.get(url)
        soup = BeautifulSoup(data.text, 'lxml')

        if class_id != None:
            imgs = soup.find_all('img', f'{class_id}')
        else:
            imgs = soup.find_all('img')

        for img in imgs:
            img_lists.append(img['src'])
    return img_lists


def download_img(url, index, ouput_dir):
    '''下載 圖片'''
    if not os.path.exists(ouput_dir):
        os.makedirs(ouput_dir)

    data = requests.get(url)
    with open(f'{ouput_dir}\{str(index).zfill(3)}.jpg', 'wb') as f:
        f.write(data.content)

    return


urls = []
class_id = ''
img_lists = get_img_list(urls, class_id=class_id)

for index in range(0, len(img_lists)):
    download_img(str(img_lists[index]), index + 1, 'D:\code\imgs')
