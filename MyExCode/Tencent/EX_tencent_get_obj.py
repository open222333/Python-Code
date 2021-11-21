from EX_tencent_base_setting import client, bucket_name
'''查詢'''


def get_obj_list(prefix="", max_item=1000):
    response = client.list_objects(
        Bucket=bucket_name,
        Prefix=prefix,
        MaxKeys=max_item
    )
    response_headers = [info for info in response]
    # 若 搜尋的目標有找到 會回傳Contents
    print(f"list_objects回傳內容:{[info for info in response]}")

    if 'Contents' not in response_headers:
        print('沒有資料')
    else:
        for obj in response['Contents']:
            print(obj)


print(get_obj_list(max_item=10))
