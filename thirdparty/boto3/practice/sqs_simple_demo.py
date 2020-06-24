import boto3


# wafClient = boto3.client('wafv2')

# def get_all_welacl(start_marker=None, webacl_list=None):
#     wafClient = boto3.client('wafv2')
#     params = None
#     if start_marker:
#         params = start_marker
#         wafListGlobal = wafClient.list_web_acls(Scope='REGIONAL', Limit=10,NextMarker=params)
#     else:
#         wafListGlobal = wafClient.list_web_acls(Scope='REGIONAL', Limit=10)
#     if webacl_list:
#         wafListGlobal['WebACLs'].extend(webacl_list)
#     while 'NextMarker' in wafListGlobal:
#         next_marker = wafListGlobal['NextMarker']
#         webacl_list = wafListGlobal['WebACLs']
#         wafListGlobal = get_all_welacl(next_marker,webacl_list)
#     return wafListGlobal

# print(get_all_welacl())



wafarn = []
# client = boto3.client('wafv2','ap-northeast-1')
client = boto3.client('waf')
# wafv2response = client.list_web_acls(Scope='REGIONAL')
response = client.list_web_acls()
print(response['WebACLs'])

for WebACLId in response["WebACLs"]:
    print(WebACLId)

# print(wafv2response)

# if bool(wafv2response):
#     for waf in wafv2response['WebACLs']:
#         wafarn.append(waf['Id'])
#         response1 = client.get_web_acl(Name=waf["Name"], Id = waf['Id'], Scope='REGIONAL')
#         # print(response1['WebACL']['Rules'])
#         for i in range(len(response1['WebACL']['Rules'])):
            
#             print("ddddddddddddddd")
#             ruleId = response1['WebACL']['Rules'][i]["Statement"]["ManagedRuleGroupStatement"]["ExcludedRules"]
            
#             print(ruleId)
#         break

# groupTemp = client.get_rule_group(Name="SizeRestrictions_QUERYSTRING")

# for wafId in wafarn:
#     print(wafId)
#     response1 = client.get_web_acl(Id = wafId)
#     print(response1)

# for waf in wafarn:
#     wafv2response = client.list_resources_for_web_acl(
#         WebACLArn=waf
#     )
#     print(wafv2response)
#     for albinwaf in wafv2response['ResourceArns']:
#         if bool(albinwaf):
#             wafnalbs.append(albinwaf)

