import re
import boto3
import botocore


class awsS3():
    def __init__(self):
        self.s3_resource = boto3.resource(
            # service_name
            's3',
            aws_access_key_id='AWS_ACCESS_KEY_ID',
            aws_secret_access_key='AWS_SECRET_ACCESS_KEY',
            # AWS地區編碼
            region_name='ap-northeast-1'
        )

    def upload_file(self, file_path_in_local, file_path_in_s3, bucket='name'):
        # 上傳檔案
        # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#bucket
        self.s3_resource.Bucket(bucket).upload_file(
            file_path_in_local, file_path_in_s3)

    def check_file_exists(self, file_path_in_s3, bucket='name'):
        # 檢查檔案是否存在
        try:
            self.s3_resource.Object(bucket, file_path_in_s3).load()
        except botocore.exceptions.ClientError as e:
            if e.respones['Error']['Code'] == '404':
                print("file not found")
            else:
                print(
                    f"Something went wrong. Http error code is {e.respones['Error']['Code']}")
            return False
        return True

    def copy(self, source_bucket, source_key, destination_bucket, destination_key):
        # 複製檔案
        copy_source = {
            'Bucket': source_bucket,
            'Key': source_key
        }
        self.s3_resource.meta.client.copy(
            copy_source, destination_bucket, destination_key)
