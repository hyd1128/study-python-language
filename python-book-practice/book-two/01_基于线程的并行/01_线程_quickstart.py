#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import threading


def function(i):
    print("function called bu thread")
    return


threads = []

for i in range(5):
    t = threading.Thread(target=function, args=(i,))
    threads.append(t)
    t.start()
    t.join()
