from scrapinghub import ScrapinghubClient


def get_SI_prefix_num(target: str):
    '''國際單位制接頭詞 SI prefix 轉為數字
    參考https://en.wikipedia.org/wiki/Metric_prefix'''
    import re
    from math import pow

    def replace_symbols(target: str, symbols: list):
        '''將符號 移除'''
        for symbol in symbols:
            if symbol in target:
                target = target.replace(symbol, '')
        return target

    SI_prefix = {
        'K': pow(10, 3),
        'M': pow(10, 6),
        'G': pow(10, 9),
        'T': pow(10, 12),
        'P': pow(10, 15),
        'E': pow(10, 18),
        'Z': pow(10, 21),
        'Y': pow(10, 24)
    }
    try:
        # 排除 ,
        symbols = [',']
        target = replace_symbols(target, symbols)

        split_str = re.findall(r'(.*)(\D)', target)[0]
        if len(split_str) != 0:
            symbol = split_str[1]
            num = float(split_str[0])

            symbol = str(symbol).upper()
            unit = SI_prefix[symbol]
            return int(round(float(num) * unit, 0))
        return int(target)
    except:
        return target


def get_scrapyhub_items(spider_code=None):
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


def is_target_tag(target_tags: list, source_tags: list) -> bool:
    for tag in source_tags:
        if tag in target_tags:
            return True
    else:
        return False
