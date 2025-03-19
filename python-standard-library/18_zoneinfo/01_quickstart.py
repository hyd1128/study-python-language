#!/usr/bin/env python
# _*_ coding: utf-8 _*_
import zoneinfo
from datetime import datetime, tzinfo
from zoneinfo import ZoneInfo

utc_now = datetime.now(ZoneInfo("UTC")).strftime("%Y-%m-%d %H:%M:%S")
print("utc time:" + str(utc_now))


# 获取当前utf时间
utc_now = datetime.now(ZoneInfo("America/New_York")).strftime("%Y-%m-%d %H:%M:%S")
print("utc time:" + str(utc_now))

utc_now = datetime(year=2021, month=8, day=1, hour=20, minute=20, second=10, tzinfo=ZoneInfo("America/New_York"))
print("utc time:" + str(utc_now))

print(ZoneInfo.key)
print(type(ZoneInfo.key))
print("UTC" in zoneinfo.available_timezones())
print("America/New_York" in zoneinfo.available_timezones())
print(type(ZoneInfo("America/New_York")))
print(isinstance(ZoneInfo("America/New_York"), tzinfo))

print(datetime.now(tz=ZoneInfo("America/New_York")))
# print(datetime.replace())