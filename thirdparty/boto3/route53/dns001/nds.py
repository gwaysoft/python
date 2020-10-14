#!/usr/bin/python3.6

import os
import json
import boto3
from botocore.client import Config

DIR = os.path.dirname(os.path.realpath(__file__))
CONFIG = json.load(open(os.path.join(DIR, 'config.json')))

print(CONFIG['aws_key_id'])
print(CONFIG['aws_key_secret'])

client = boto3.client(
    'route53',
    aws_access_key_id=CONFIG['aws_key_id'],
    aws_secret_access_key=CONFIG['aws_key_secret']
)
# client = boto3.client('route53domains',
#                       aws_access_key_id=CONFIG['aws_key_id'],
#                       aws_secret_access_key=CONFIG['aws_key_secret']
#                       )
# response = client.list_domains()
#
# print(response)
response = client.list_hosted_zones()

print(type(response), response)
print(json.dumps(response))
