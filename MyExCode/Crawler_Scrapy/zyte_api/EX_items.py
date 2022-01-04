from scrapinghub import ScrapinghubClient
import json
'''
使用官方的模組

API文檔
https://docs.zyte.com/scrapy-cloud/items.html

scrapinghub 文檔
https://python-scrapinghub.readthedocs.io/en/latest/

api_key = xxxxxxxxxxxxx
project_id = 123456
job_id = 123456/2/2
'''

# 範例
# https://storage.scrapinghub.com/items/53/34/7
# items/:project_id[/:spider_id][/:job_id][/:item_no][/:field_name]


def get_zyte_activity(api_key, project_id):
    client = ScrapinghubClient(api_key)
    activity = client.get_project(project_id).activity.iter()
    return activity


def get_zyte_spiders_id(api_key, project_id):
    client = ScrapinghubClient(api_key)
    spiders = client.get_project(project_id).spiders.iter()
    results = [i['id'] for i in spiders]
    return results


def get_zyte_jobs_id(api_key, project_id):
    client = ScrapinghubClient(api_key)
    jobs = client.get_project(project_id).jobs.iter()
    results = [(i['spider'], i['key']) for i in jobs]
    return results


def get_zyte_items(api_key, project_id, job_id):
    client = ScrapinghubClient(api_key)
    project = client.get_project(project_id)
    job = project.jobs.get(job_id)
    items = job.items.iter()
    return items


def get_items(spider_code=None):
    '''spider_code: 沒指定，回傳現有全部爬蟲'''

    def get_job_id(key_1: str, key_2: str):
        key_1 = key_1.split('/')
        key_2 = key_2.split('/')
        num = max(key_1[2], key_2[2])
        job_key = f'{key_1[0]}/{key_1[1]}/{num}'
        return job_key
    api_key = ''
    project_id = ''
    client = ScrapinghubClient(api_key)
    jobs = client.get_project(project_id).jobs.iter()

    target = {}
    for job in jobs:

        if spider_code != None:
            target[spider_code] = ''

        if job['spider'] in target:
            key_1 = target[job['spider']]
            key_2 = job['key']
            target[job['spider']] = get_job_id(key_1, key_2)
        else:
            if spider_code == None:
                target[job['spider']] = job['key']
            else:
                pass

    data = {}
    for spider, job_key in target.items():
        items = client.get_job(job_key).items.list()
        data[spider] = items

    return data


def create_json_file(data, fileName='data.json'):
    with open(fileName, 'w', newline='') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


data = get_items()
