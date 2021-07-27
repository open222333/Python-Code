import requests

url = 'https://docs.google.com/forms/d/e/1FAIpQLSc7fZg0bAjD5fQOsdxtIHlV3m-OPECu3VHahfJYJH2_-KGCmQ/viewform'
text = requests.get(url)
print(text.headers)