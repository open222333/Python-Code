import boto3

class awsS3():
    def __init__(self):
        self.s3_resource = boto3.resource(
            # service_name
            's3',
            aws_access_key_id='AWS_ACCESS_KEY_ID',aws_secret_access_key='AWS_SECRET_ACCESS_KEY',
            # AWS地區編碼
            region_name='ap-northeast-1'
        )

    def upload_file(self):
        self.s3_resource.Bucket()
        pass
