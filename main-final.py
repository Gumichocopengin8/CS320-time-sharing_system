# Keita Nonaka
# Nick Smith
# Kyle Wyse
# Koki Omori
# 30 Sep 2018
# OS Simulation

# Project Description: 
#
#


import queue


class Process:
    def __init__(self, name, time):
        self.name = name
        self.time = time

output = ''

with open('test.txt','r') as file:
    ele = file.readline().split()
    eleNum = int(ele[0]) # number of process
    TASK_TIME_LIMIT = int(ele[1]) 

    tasks = queue.Queue() # queue
    for i in range(0, eleNum):
        stringArray = file.readline().split()
        process = Process(stringArray[0], int(stringArray[1]))
        tasks.put(process)

    CPUTime = 0 #clock ticks
    while not tasks.empty(): # while have processes
        CPUTime += 1 #OVERHEAD for selecting a program (running dispatcher)
        process = tasks.get() # get next process on queue
        CPUTime += 3 #OVERHEAD for loading a process
        output += ("{0:>5} {1:>10}: put on processor \n".format(CPUTime, process.name))
        CPUTime += process.time if process.time < TASK_TIME_LIMIT else TASK_TIME_LIMIT
        process.time -= TASK_TIME_LIMIT
        if process.time > 0: # if process is not done
            tasks.put(process) # put it back on the queue
            CPUTime += 3 #OVERHEAD for saving an incomplete process
            output += "{1:>5} {0:>10}: Time left for process: {2:>5} \n".format(process.name, CPUTime, process.time)
        else:
            output += "{1:>5} {0:>10}: {2} is complete \n".format(process.name, CPUTime, process.name)
    output += ("Complete time is {0}\n".format(CPUTime))
    
    with open('output.txt', 'w') as outFile:
        outFile.write(output)