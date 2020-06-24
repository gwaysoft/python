import boto3

s3_client = boto3.client("s3")

# for bucket in s3.buckets.all():
#     print(bucket.name)
#     for obj in bucket.objects.all():
#         print(obj.key)

bucket = "demo-s3-bucket-qq"
key = "test.txt"

s3_client.put_object(Bucket=bucket, Key=key, Body=b"dddd")

obj = s3_client.get_object(Bucket=bucket, Key=key)
print(obj["Body"].read())
