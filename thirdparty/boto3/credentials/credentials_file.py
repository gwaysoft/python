import boto3

credentials = ("default", "other")

for cred in credentials:
    print(cred)
    session = boto3.Session(profile_name=cred)
    s3 = session.resource('s3')
    for bucket in s3.buckets.all():
        print(bucket.name)
        # for obj in bucket.objects.all():
        #     print(obj.key)