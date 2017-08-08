#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com
from multiprocessing import Process
import random
import time
# import os
# print(os.cpu_count())

"""
执行程序就会生成一个主线程

"""


def task(name):
    print('%s is doing task' % name)
    time.sleep(random.randint(1, 3))
    print('%s has finished the task' % name)


if __name__ == '__main__':
    p1 = Process(target=task, args=('linda',), name='p1')
    p1.start()  # 发系统调用，让OS建进程，父进程不等
    print('p1 name: ', p1.name)
    # time.sleep(1)
    print('父进程')
