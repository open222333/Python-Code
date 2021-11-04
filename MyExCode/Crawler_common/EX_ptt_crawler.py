# ptt的url規律：https://www.ptt.cc/bbs/<看板名稱>/index.html
import requests
from bs4 import BeautifulSoup

broad_name = "Stock"
url = f"https://www.ptt.cc/bbs/{broad_name}/index.html"


def get_all_href(url) -> list:
    # 取得鏈結
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    results = soup.select("div.title")
    results_list = []
    for item in results:
        try:
            a_item = item.select_one("a")
            title = item.text.replace("\n", "")
            # 有的是空值 None
            if a_item:
                results_list.append(
                    (title, 'https://www.ptt.cc' + a_item.get('href')))
        except:
            pass
    return results_list


def get_article_content(url):
    # 取得內容
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    results = soup.select('span.article-meta-value')
    return (results[0].text, results[1].text, results[2].text, results[3].text)


for page in range(1, 4):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    btn = soup.select("div.btn-group > a")  # 用>的話，是只要下一層的
    # print(btn)
    # [<a class="btn selected" href="/bbs/Stock/index.html">看板</a>, <a class="btn" href="/man/Stock/index.html">精華區</a>, <a class="btn wide" href="/bbs/Stock/index1.html">最舊</a>, <a class="btn wide" href="/bbs/Stock/index5000.html">‹ 上頁</a>, <a class="btn wide" href="/bbs/Stock/index5002.html">下頁 ›</a>, <a class="btn wide" href="/bbs/Stock/index.html">最新</a>]
    up_page_href = btn[3]['href']
    next_page_url = 'https://www.ptt.cc' + up_page_href
    url = next_page_url
    href = get_all_href(url)
    for i in href:
        print(f"{i[0]}\n{get_article_content(i[1])}")
    print('------------------ next page ------------------')
