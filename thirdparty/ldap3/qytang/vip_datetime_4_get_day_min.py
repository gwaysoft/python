#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

from datetime import datetime, date

now = datetime.now()

# 日期
print(now.date())
# 星期
print(now.weekday())
# 年
print(now.year)
# 月（有時候要加一個月）
print(now.month)
# 天
print(now.day)
# 秒
print(now.second)
# 分鐘
print(now.minute)

def next_month(date):
    new_year = date.year
    new_month = date.month + 1
    # note: in datetime.date, months go from 1 to 12
    if new_month > 12:
        new_year += 1
        new_month -= 12
    new_date = date.replace(month=new_month, year=new_year)
    return new_date


def before_month(date):
    new_year = date.year
    new_month = date.month - 1
    # note: in datetime.date, months go from 1 to 12
    if new_month == 0:
        new_year -= 1
        new_month += 12
    new_date = date.replace(month=new_month, year=new_year)
    return new_date

print(next_month(date.today()))
print(before_month(date.today()))

# 一個月有幾天
import calendar
print(calendar.monthrange(now.year, now.month))

# 獲得月份英文名
print(calendar.month_name[11])

# 英文名到數字
s = 'March'
d = datetime.strptime(s, '%B')
print(d.strftime('%m'))

