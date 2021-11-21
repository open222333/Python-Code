from EX_tencent_base_setting import client, bucket_name
from qcloud_cos import CosServiceError
import traceback


def is_tencent_obj_exists(bucket, key):
    try:
        client.head_object(Bucket=bucket, Key=key)
        return True
    except CosServiceError:
        return False
    except Exception:
        print(traceback.format_exc())


key = 'fulifan/FULIFAN-2108/h264/FULIFAN-2108-240_00020.ts'
# key = 'dddddd'
print(is_tencent_obj_exists(bucket_name, key))
