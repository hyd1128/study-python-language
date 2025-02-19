#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import threading
import time


def first_function():
    print(threading.current_thread().name + str(' is Starting '))
    time.sleep(2)
    print(threading.current_thread().name + str(' is Exiting '))
    return


def second_function():
    print(threading.current_thread().name + str(' is Starting '))
    time.sleep(2)
    print(threading.current_thread().name + str(' is Exiting '))
    return


def third_function():
    print(threading.current_thread().name + str(' is Starting '))
    time.sleep(2)
    print(threading.current_thread().name + str(' is Exiting '))
    return


if __name__ == "__main__":
    t1 = threading.Thread(name='first_function', target=first_function)
    t2 = threading.Thread(name='second_function', target=second_function)
    t3 = threading.Thread(name='third_function', target=third_function)
    t1.start()
    t2.start()
    t3.start()
