# https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html
import boto3

# s3 = boto3.resource("s3")
# name = s3.Bucket("demo-s3-bucket-qq").name
# print(name)


# isFrist = True
# for bucket in s3.buckets.all():
#     print(bucket.name)
#     if isFrist:
#         isFrist = False
#         data = open("readme.md", mode="rb")
#         # udpate a file
#         bucket.put_object(Key="readme.md", Body=data)
#         print("update for ", bucket.name)

# s3 = boto3.resource('s3', config=Config(signature_version='s3v4'))

ec2 = boto3.resource("ec2")
for i in ec2.instances.all():
    if i.state["Name"] == "stopped":
        print(i.state, i.cpu_options, i.instance_id, i.vpc_id, i.subnet_id, i.private_ip_address, i.tags)
        print(i.key_pair, i.vpc)
        response = i.create_tags(
            DryRun=False,
            Tags = [
                {
                    "Key":"instance_sdk",
                    "Value":"from sdk"
                }
            ]
        )

