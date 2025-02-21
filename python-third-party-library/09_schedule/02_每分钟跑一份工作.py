#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import schedule
import time


def job():
    print("I am working")


schedule.every(3).seconds.do(job)


while True:
    schedule.run_pending()
    time.sleep(1)

