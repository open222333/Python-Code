import requests
import shutil

url = ''
# stream=True 強制解壓縮
r = requests.get(url, stream=True, timeout=1)
file_name = url.split("/")[-1]
with open(file_name, "wb") as f:
    shutil.copyfileobj(r.raw, f)
