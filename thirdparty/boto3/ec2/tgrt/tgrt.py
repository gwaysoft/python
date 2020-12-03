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
    region_name='ap-northeast-1'
)
# client = boto3.client('route53domains',
#                       aws_access_key_id=CONFIG['aws_key_id'],
#                       aws_secret_access_key=CONFIG['aws_key_secret']
#                       )
# response = client.list_domains()
#
# print(response)

# response = client.describe_vpcs()

# print(type(response), response)

response = client.describe_transit_gateway_route_tables()["TransitGatewayRouteTables"]
print(response)
for item in response:
    print(item)
print("---------")
response = client.describe_transit_gateway_attachments()['TransitGatewayAttachments']
print(response)
for item in response:
    print(item)

response = client.describe_transit_gateway_attachments(TransitGatewayAttachmentIds=[
    'tgw-attach-0c4f1a03619629ab5'
])

# print(type(response), response)
for key, value in response.items():
    print(key, value)
# print(tgai["TransitGatewayId"] + "")

for item in response['TransitGatewayAttachments']:
    print(item["TransitGatewayId"])


# Create transit gateway route
def create_transit_gateway_route(client, transit_gateway_rt_id, destination_ip_block, transit_gateway_attachment_id):
    # client = boto3.client('ec2', region_name='us-east-1')
    response = client.create_transit_gateway_route(
        DestinationCidrBlock=destination_ip_block,
        TransitGatewayRouteTableId=transit_gateway_rt_id,
        TransitGatewayAttachmentId=transit_gateway_attachment_id,
        Blackhole=False,
        DryRun=False
    )
    return response

response = client.get_transit_gateway_prefix_list_references(TransitGatewayRouteTableId='tgw-rtb-070082d3566750a94')
print(response)
for item in response:
    print(item)


# response = client.export_transit_gateway_routes(TransitGatewayRouteTableId='tgw-rtb-0c9dc9f05eae05993')
# print(response)
# for item in response:
#     print(item)
#
# print(
#     create_transit_gateway_route(client, "tgw-rtb-070082d3566750a94", '192.168.0.0/24', "tgw-attach-0c4f1a03619629ab5"))


# response = client.delete_transit_gateway_route(
#     TransitGatewayRouteTableId='tgw-rtb-070082d3566750a94',
#     DestinationCidrBlock='192.168.0.0/24',
#     DryRun=False
# )


# response = client.replace_transit_gateway_route(
#     DestinationCidrBlock='172.31.0.0/20',
#     TransitGatewayRouteTableId='tgw-rtb-070082d3566750a94',
#     TransitGatewayAttachmentId='tgw-attach-0c4f1a03619629ab5',
#     Blackhole=True,
#     DryRun=False
# )


response = client.search_transit_gateway_routes(
    TransitGatewayRouteTableId='tgw-rtb-070082d3566750a94',
    Filters=[
        {
            'Name': 'type',
            'Values': [
                'static', 'propagated'
            ]
        },
    ],
    MaxResults=123,
    DryRun=False
)

for item in response["Routes"]:
    print(item)
