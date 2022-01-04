import requests


'''使用註冊為用戶名後獲得的API密鑰；將密碼留空。

curl \
   --user YOUR_API_KEY: \
   --header 'Content-Type: application/json' \
   --data '{"url": "https://example.com/foo/bar", "browserHtml": true}' \
   https://api.zyte.com/v1/extract
   
https://docs.zyte.com/scrapy-cloud/items.html#items-project-id-spider-id-job-id-item-no-field-name

https://docs.zyte.com/scrapy-cloud/items.html#items-project-id-spider-id-job-id-item-no-field-name
'''

api_key = ''
project_id = ''
jobs_id = ''
url = f'https://storage.scrapinghub.com/items/{project_id}/{jobs_id}'
response = requests.get(url, auth=(api_key, ''))
