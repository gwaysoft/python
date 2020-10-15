#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a
from datetime import datetime, date, timedelta
from dateutil import parser
start_datetime = datetime.now() - timedelta(days=7, minutes=6, seconds=6)
start_date = date.today() - timedelta(days=7)

print(start_datetime)
print(start_date)

end_date = parser.parse('2020-3-16 18:15:00')

delta_datetime = end_date - datetime.now()
print(delta_datetime)
print(delta_datetime.days)
print(delta_datetime.seconds)
print(delta_datetime.total_seconds())


# Django 時間過濾
# time__gte
# sec_student_anyconnect_weeky = AnyconnectLogin.objects.filter(group_policy='secnp-group-policy', account_type='Stop', time__gte=d.astimezone(tzutc_8))

# check_time__lte
# old_homework = SecHomeWork.objects.filter(check_time__lte=d.astimezone(tzutc_8), homework_checked__isnull=False)