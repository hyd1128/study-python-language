#!/usr/bin/env python
# _*_ coding: utf-8 _*_


import threading

shared_resource_with_lock = 0
shared_resource_with_no_lock = 0
COUNT = 100
shared_resource_lock = threading.Lock()


# 有锁的情况
def increment_with_lock():
    global shared_resource_with_lock
    for i in range(COUNT):
        shared_resource_lock.acquire()
        # shared_resource_with_lock += 1
        print("111")
        shared_resource_lock.release()


def decrement_with_lock():
    global shared_resource_with_lock
    for i in range(COUNT):
        shared_resource_lock.acquire()
        # shared_resource_with_lock -= 1
        print("222")
        shared_resource_lock.release()


# 没有锁的情况
def increment_without_lock():
    global shared_resource_with_no_lock
    for i in range(COUNT):
        # shared_resource_with_no_lock += 1
        print("333")

def decrement_without_lock():
    global shared_resource_with_no_lock
    for i in range(COUNT):
        # shared_resource_with_no_lock -= 1
        print("444")


if __name__ == "__main__":
    # t1 = threading.Thread(target=increment_with_lock)
    # t2 = threading.Thread(target=decrement_with_lock)
    t3 = threading.Thread(target=increment_without_lock)
    t4 = threading.Thread(target=decrement_without_lock)
    # t1.start()
    # t2.start()
    t3.start()
    t4.start()
    # t1.join()
    # t2.join()
    t3.join()
    t4.join()
    print("the value of shared variable with lock management is %s" % shared_resource_with_lock)
    print("the value of shared variable with race condition is %s" % shared_resource_with_no_lock)

    """
        通过这个例子可以看出加锁和不加锁是存在的区别
    """
