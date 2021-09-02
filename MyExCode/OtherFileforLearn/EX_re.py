import re

testdata = ["window.open('https://99jp.live/9pza0');gtag('event', '免费国产资源-1', { 'event_category': '首页-精品视频应用', 'event_label': 'https://99jp.live/9pza0' });", "window.open('https://dq1i.cn');gtag('event', '精东视频破解-2', { 'event_category': '首页-精品视频应用', 'event_label': 'cpa-https://dq1i.cn' });",
            "window.open('https://hycapp1.club/hgdh');gtag('event', '盘她色狗-3', { 'event_category': '首页-精品视频应用', 'event_label': 'https://hycapp1.club/hgdh' });", "window.open('http://sxaxy.com/pjboadhfl');gtag('event', '日女束缚视频-4', { 'event_category': '首页-精品视频应用', 'event_label': 'http://sxaxy.com/pjboadhfl' });"]
# rule = r"[a-zA-Z]+://[^\s]*[$;]"
# for i in testdata:
#     m = re.search(rule ,i)
#     print(m.group().replace("');", ""))

for data in testdata:
    da = re.search(r"[a-zA-Z]+://[^\s']*", data)
    print(da.group(), type(da))
