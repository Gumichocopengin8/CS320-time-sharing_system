# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 15:16:01 2018

@author: kyled
"""

import queue


class Process:
    def __init__(self, name, processTime):
        self.name = name
        self.processTime = processTime
        

with open('test.txt','r') as file:
    
    ele = file.readline().split()
    eleNum = int(ele[0])
    TASK_TIME_LIMIT = int(ele[1])

    que = queue.Queue() 
    for i in range(0, TASK_TIME_LIMIT):
        stringArray = file.readline().split()
        process = Process(stringArray[0], int(stringArray[1]))
        que.put(process)

    CPUTime = 0
    while que.qsize() > 0:
        process = que.get()
        CPUTime += TASK_TIME_LIMIT
        process.processTime -= TASK_TIME_LIMIT
        print("{0} {1}".format(process.name, CPUTime))
        print("ran for >= 40 seconds")
        if process.processTime > 0:
            que.put(process)
            continue

        CPUTime += process.processTime
        print("{0} {1}".format(process.name, CPUTime))