from EX_tencent_base_setting import client, bucket_name
from qcloud_cos import CosServiceError
import traceback
'''查詢'''


def get_obj(bucket, key):
    try:
        result = client.head_object(Bucket=bucket, Key=key)
    except CosServiceError as err:
        print(err.get_error_code(), err.get_error_msg())
        return False
    return result


def get_obj_list(bucket, prefix="", max_item=1000) -> dict:
    '''取得騰訊雲資料目前有的檔案 回傳所有 key:size'''
    stock = {}
    response = client.list_objects(
        Bucket=bucket,
        Prefix=prefix,
        MaxKeys=max_item
    )
    response_headers = [info for info in response]
    # 若 搜尋的目標有找到 會回傳Contents
    # print(f"list_objects回傳內容:{[info for info in response]}")

    if 'Contents' not in response_headers:
        print(response)
        print('沒有資料')
        return None
    else:
        for obj in response['Contents']:
            # print(obj)
            stock[obj['Key']] = obj['Size']
        return stock


def upload_to_tencent(remote_file, local_file):
    '''上傳檔案'''
    try:
        client.upload_file(
            Bucket=bucket_name,
            Key=remote_file,
            LocalFilePath=local_file
        )
    except:
        traceback.print_exc()
        return False
    return True


def is_tencent_obj_exists(bucket, key):
    '''
    檢查AWS的檔案是否已上傳至騰訊雲且是否完整 若是 回傳檔案訊息
    bucket: 存儲桶
    key: 檔案路徑
    '''
    try:
        if client.object_exists(bucket, key):
            return client.head_object(bucket, key)
        else:
            return False
    except Exception:
        print(traceback.format_exc())


key = 'anchor/ANCHOR-00001/h264/ANCHOR-00001-240.m3u8'
size = is_tencent_obj_exists(bucket_name, key)['Content-Length']
print(type(size))
