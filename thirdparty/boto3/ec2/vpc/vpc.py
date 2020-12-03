#!/usr/bin/python3.6

import os
import json
import boto3
from botocore.client import Config

DIR = os.path.dirname(os.path.realpath(__file__))
CONFIG = json.load(open(os.path.join(DIR, '../config.json')))

print(CONFIG['aws_access_key_id'])
print(CONFIG['aws_secret_access_key'])

client = boto3.client(
    'ec2',
    aws_access_key_id=CONFIG['aws_access_key_id'],
    aws_secret_access_key=CONFIG['aws_secret_access_key'],
    region_name=CONFIG['region_name']
)
# client = boto3.client('route53domains',
#                       aws_access_key_id=CONFIG['aws_key_id'],
#                       aws_secret_access_key=CONFIG['aws_key_secret']
#                       )
# response = client.list_domains()
#
# print(response)
# response = client.describe_transit_gateway_route_tables()["TransitGatewayRouteTables"]
response = client.describe_vpcs()

for item in response['Vpcs']:
    print(item)
#
# print(type(response), response)
# print(json.dumps(response))


# tgw_us_east_1 = (paginator['TransitGateways'][0]['TransitGatewayId'])
# account_id = (paginator['TransitGateways'][0]['OwnerId'])
# print(tgw_us_east_1, account_id)
