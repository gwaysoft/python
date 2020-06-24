import boto3

from botocore.response import StreamingBody

s3 = boto3.resource("s3")

# for bucket in s3.buckets.all():
#     print(bucket.name)
#     for obj in bucket.objects.all():
#         print(obj.key)

bucket = "demo-s3-bucket-qq"
key = "test.txt"
obj = s3.Object(bucket, key)

stream = obj.get()["Body"]

if stream is not None:
    data = stream.read().decode("utf-8")
    print(data)

stream.close()
some_binary_data = b'Here we have some data'
obj.put(Body=some_binary_data)


