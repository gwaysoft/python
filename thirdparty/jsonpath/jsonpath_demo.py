import jsonpath

rules = [{
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
                        {'Name': 'NoUserAgent_HEADER'
                         },
                        {'Name': 'UserAgent_BadBots_HEADER'
                         },
                        {'Name': 'EC2MetaDataSSRF_BODY'
                         },
                        {'Name': 'EC2MetaDataSSRF_URIPATH'
                         }
                    ]
                }
            },
    "OverrideAction": {
                "None": {}
            },
    "VisibilityConfig": {
                "SampledRequestsEnabled": True,
                "CloudWatchMetricsEnabled": True,
                "MetricName": "AWS-AWSManagedRulesCommonRuleSet001"
            }
}, {'Name': 'AWS-AWSManagedRulesAnonymousIpList', 'Priority': 1, 'Statement': {'ManagedRuleGroupStatement': {'VendorName': 'AWS', 'Name': 'AWSManagedRulesAnonymousIpList', 'ExcludedRules': [
    {'Name': 'AnonymousIPList'
     }
]
}
}, 'OverrideAction': {'Count': {}
                      }, 'VisibilityConfig': {'SampledRequestsEnabled': True, 'CloudWatchMetricsEnabled': True, 'MetricName': 'AWS-AWSManagedRulesAnonymousIpList'
                                              }
}]

# nameList = jsonpath.jsonpath(
#     rules, "$.[0].Statement.ManagedRuleGroupStatement.ExcludedRules..Name")


nameList = jsonpath.jsonpath(
    rules, "$.*")
# for i in nameList:
#     nameList = jsonpath.jsonpath(
#         i, "$.Statement.ManagedRuleGroupStatement.ExcludedRules..Name")
#     print(nameList)

# changeList = jsonpath.jsonpath(
#         rules, "$.[0],Statement.ManagedRuleGroupStatement.ExcludedRules")

# rules[0]["Statement"]["ManagedRuleGroupStatement"]["ExcludedRules"] = jsonpath.jsonpath(
#         rules, "$.[1],Statement.ManagedRuleGroupStatement.ExcludedRules")

changeList = jsonpath.jsonpath(
        rules, "$.[1]..ExcludedRules.*")

origin = rules[0]["Statement"]["ManagedRuleGroupStatement"]["ExcludedRules"]
print(changeList)
print(origin)

rules[0]["Statement"]["ManagedRuleGroupStatement"]["ExcludedRules"] = changeList
origin = rules[0]["Statement"]["ManagedRuleGroupStatement"]["ExcludedRules"]
print(rules)
# print(nameList)
