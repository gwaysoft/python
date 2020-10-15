#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

from datetime import datetime, timezone, timedelta

tzutc_8 = timezone(timedelta(hours=8))  # 设置时区为东八区
tzutc_0 = timezone(timedelta(hours=0))  # 设置时区为格林威治

now = datetime.now()

# 默認為系統時區
print(now)

print(now.astimezone(tzutc_8))
print(now.astimezone(tzutc_0))