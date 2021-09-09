import re


def get_content(pattern, file):
    with open(file, 'r') as f:
        text = f.read()
    results = set(re.findall(pattern, text))
    return results


pattern = r'<iframe src=+[^\s]*[^ "]'
urls_pattern = r'[a-zA-Z]+://+[^\s]*'
print(get_content(pattern, 'test_video_1.html'))
# for i in get_content(pattern, 'test_video_1.html'):
#     print(re.findall(urls_pattern, i))
