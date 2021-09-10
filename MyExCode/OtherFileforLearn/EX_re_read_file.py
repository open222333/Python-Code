import re


def get_content(pattern, file):
    with open(file, 'r') as f:
        text = f.read()
    results = set(re.findall(pattern, text))
    return results


pattern = r'<iframe src=+[^\s]*[^ "]'
iframe_pattern = r"html5player.setVideoURL+[^\s]*[^');]"
urls_pattern = r'[a-zA-Z]+://+[^\s]*'
urls2_pattern = r"/+[^\s]*[^');\n]"
print(get_content(iframe_pattern, 'test_1.html'))
for i in get_content(iframe_pattern, 'test_1.html'):
    print(re.findall(urls2_pattern, i))
