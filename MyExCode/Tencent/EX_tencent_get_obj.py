from EX_tencent_base_setting import client, bucket_name
from qcloud_cos import CosServiceError
'''查詢'''


def get_obj(bucket, key):
    try:
        result = client.head_object(Bucket=bucket, Key=key)
    except CosServiceError as err:
        print(err.get_error_code(), err.get_error_msg())
        return False
    return result


def get_obj_list(bucket, prefix="", max_item=1000) -> dict:
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


# print(get_obj_list(max_item=10))
key = 'madou/MADOU-00069'
result = get_obj_list(bucket_name, key)
print('madou/MADOU-00069/h264/MADOU-00069-240_00243.ts' in result.keys())
