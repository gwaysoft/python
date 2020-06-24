import boto3

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
}]


wafv2_client = boto3.client('wafv2', 'ap-northeast-1')

response = wafv2_client.create_web_acl(Name="custom-waf",
                                       Scope="REGIONAL",
                                       DefaultAction={'Allow': {}},
                                       Description="custom waf 001",
                                       Rules=rules,
                                       VisibilityConfig={
                                           "SampledRequestsEnabled": True,
                                           "CloudWatchMetricsEnabled": True,
                                           "MetricName": "AWS-AWSManagedRulesCommonRuleSet001"
                                       },
                                       Tags=[
                                           {"Key": "Name",
                                            "Value": "custom-tag"}
                                       ])
print(response)
