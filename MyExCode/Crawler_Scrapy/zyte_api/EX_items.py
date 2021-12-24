from scrapinghub import ScrapinghubClient
'''https://docs.zyte.com/scrapy-cloud/items.html'''

# 範例
# https://storage.scrapinghub.com/items/53/34/7
# items/:project_id[/:spider_id][/:job_id][/:item_no][/:field_name]
api_key = ''
project_id = 575144
job_id = f'{project_id}/{2}/{2}'
client = ScrapinghubClient(api_key)
project = client.get_project(project_id)
job = project.jobs.get(job_id)
items = job.items.list()
for i in items:
    print(i)
