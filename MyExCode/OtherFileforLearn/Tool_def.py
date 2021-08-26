# 自製通用函式

def get_status_code(img_path) -> int:
    '''測試鏈結 回傳http code'''
    import requests
    return requests.get(img_path).status_code
