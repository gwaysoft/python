import os
import json
import boto3



DIR = os.path.dirname(os.path.realpath(__file__))
CONFIG = json.load(open(os.path.join(DIR, 'config.json')))

print(CONFIG['aws_access_key_id'])
print(CONFIG['aws_secret_access_key'])

s3 = boto3.client(
    's3',
    aws_access_key_id=CONFIG['aws_access_key_id'],
    aws_secret_access_key=CONFIG['aws_secret_access_key']
    # region_name=CONFIG['region_name']
)

# s3 = boto3.client("s3")

print(s3.list_buckets())

for bucket in s3.list_buckets()["Buckets"]:
    print(bucket)

# for bucket in s3.buckets.all():
#     print(bucket.name)
#     for obj in bucket.objects.all():
#         print(obj.key)

# bucket = "demo-s3-bucket-qq"
# key = "test.txt"
#
# s3_client.put_object(Bucket=bucket, Key=key, Body=b"dddd")
#
# obj = s3_client.get_object(Bucket=bucket, Key=key)
# print(obj["Body"].read())
