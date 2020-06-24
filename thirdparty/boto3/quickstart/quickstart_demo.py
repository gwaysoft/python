import boto3

s3 = boto3.resource("s3")

name = s3.Bucket("demo-s3-bucket-qq").name
print(name)


# isFrist = True
# for bucket in s3.buckets.all():
#     print(bucket.name)
#     if isFrist:
#         isFrist = False
#         data = open("readme.rm", mode="rb")
#         # udpate a file
#         bucket.put_object(Key="readme.rm", Body=data)
#         print("update for ", bucket.name)

