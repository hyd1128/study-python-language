# #!/usr/bin/env python
# # _*_ coding: utf-8 _*_
#
# # -*- coding: utf-8 -*-
#
# """Using a Semaphore to synchronize threads"""
# import threading
# import time
# import random
#
# # The optional argument gives the initial value for the internal
# # counter;
# # it defaults to 1.
# # If the value given is less than 0, ValueError is raised.
# semaphore = threading.Semaphore(0)
#
# def consumer():
#         print("consumer is waiting.")
#         # Acquire a semaphore
#         semaphore.acquire()
#         # The consumer have access to the shared resource
#         print("Consumer notify : consumed item number %s " % item)
#
# def producer():
#         global item
#         time.sleep(10)
#         # create a random item
#         item = random.randint(0, 1000)
#         print("producer notify : produced item number %s" % item)
#          # Release a semaphore, incrementing the internal counter by one.
#         # When it is zero on entry and another thread is waiting for it
#         # to become larger than zero again, wake up that thread.
#         semaphore.release()
#
# if __name__ == '__main__':
#         for i in range (0,5) :
#                 t1 = threading.Thread(target=producer)
#                 t2 = threading.Thread(target=consumer)
#                 t1.start()
#                 t2.start()
#                 t1.join()
#                 t2.join()
#         print("program terminated")

# demo
import threading
import time

# 创建一个信号量，初始值为 2
semaphore = threading.Semaphore(2)

def worker(thread_id):
    print(f"线程 {thread_id} 尝试获取信号量...")
    with semaphore:  # 自动调用 acquire() 和 release()
        print(f"线程 {thread_id} 获取到信号量，开始工作")
        time.sleep(2)  # 模拟工作
        print(f"线程 {thread_id} 工作完成，释放信号量")

# 创建并启动 4 个线程
threads = []
for i in range(4):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()

# 等待所有线程完成
for t in threads:
    t.join()
