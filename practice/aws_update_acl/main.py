import boto3
import json

# ap-northeast-1 is Asia Pacific (Tokyo)
wafv2_client = boto3.client('wafv2', 'ap-northeast-1')
wafv2_response = wafv2_client.list_web_acls(Scope='REGIONAL')


if wafv2_response is not None:
    for waf in wafv2_response['WebACLs']:
        print(waf["Name"])
        wacl_response = wafv2_client.get_web_acl(
            Name=waf["Name"], Id=waf['Id'], Scope='REGIONAL')
        print(wacl_response)
        rules = wacl_response['WebACL']['Rules']
        print(rules)