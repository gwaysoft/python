import boto3
import json

# ap-northeast-1 is Asia Pacific (Tokyo)
wafv2_client = boto3.client('wafv2', 'ap-northeast-1')
wafv2_response = wafv2_client.list_web_acls(Scope='REGIONAL')


if wafv2_response is not None:
    for waf in wafv2_response['WebACLs']:

        if waf["Name"] != "waf-test":
            continue
        print(waf["Name"])
        wacl_response = wafv2_client.get_web_acl(
            Name=waf["Name"], Id=waf['Id'], Scope='REGIONAL')
        # print(wacl_response)
        rules = wacl_response['WebACL']['Rules']
        # print(rules)

        blacklist = [{
            "Name": "AWS-AWSManagedRulesCommonRuleSet",
            "Priority": 0,
            "Statement": {
                "ManagedRuleGroupStatement": {
                    "VendorName": "AWS",
                    "Name": "AWSManagedRulesCommonRuleSet",
                    "ExcludedRules": [
                        {'Name': 'SizeRestrictions_Cookie_HEADER'
                         },
                        {'Name': 'SizeRestrictions_BODY'
                         },
                        {'Name': 'SizeRestrictions_QUERYSTRING'
                         },
                        # {'Name': 'NoUserAgent_HEADER'
                        #  },
                        {'Name': 'UserAgent_BadBots_HEADER'
                         },
                        {'Name': 'EC2MetaDataSSRF_BODY'
                         }
                        # ,
                        # {'Name': 'EC2MetaDataSSRF_URIPATH'
                        #  }
                    ]
                }
            },
            "OverrideAction": {
                "None": {}
            },
            "VisibilityConfig": {
                "SampledRequestsEnabled": True,
                "CloudWatchMetricsEnabled": True,
                "MetricName": "AWS-AWSManagedRulesCommonRuleSet1"
            }
        }]

        bj_str = json.dumps(blacklist)
        bj = json.loads(bj_str)

        print(bj, type(bj))
        # rules.append(blacklist)
        # print(rules,type(rules))
        # break
        re = wafv2_client.update_web_acl(
            Name=waf["Name"],
            Id=waf['Id'],
            Scope='REGIONAL',
            DefaultAction={'Allow': {}},
            Rules=bj,
            LockToken=wacl_response['LockToken'],
            VisibilityConfig=wacl_response['WebACL']['VisibilityConfig']
        )
        print(re)

        # print(response1['WebACL']['Rules'])
        # for i in range(len(response1['WebACL']['Rules'])):

        #     print("ddddddddddddddd")
        #     ruleId = response1['WebACL']['Rules'][i]["Statement"]["ManagedRuleGroupStatement"]["ExcludedRules"]

        #     print(ruleId)
