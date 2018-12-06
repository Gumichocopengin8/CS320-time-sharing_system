# Keita Nonaka
# Nick Smith
# Kyle Wyse
# Koki Omori
# 30 Sep 2018
# OS Simulation

# This program Simulates a Time Sharing Operating System

# It takes an input file 'input.txt.' to run. The format of the input file should be as follows:
# <number of tasks> <CPU time limit>
# <job1 name> <job1 total time>
# <jobN name> <jobN total time>

# It will also provide an output file named 'auditLog.txt'


import queue


class Process:
    def __init__(self, name, time):
        self.name = name
        self.time = time
        self.waitT = 0
        self.servT = time


with open('test.txt','r') as file: # read file
    auditLog = '{0:>5} {1:>10} {2:>5} \n\n'.format('Time', 'PID', 'log') # for output.txt file
    ele = file.readline().split()
    eleNum = int(ele[0]) # number of process
    TASK_TIME_LIMIT = int(ele[1]) 

    tasks = queue.Queue() # queue
    for i in range(0, eleNum):
        stringArray = file.readline().split()
        process = Process(stringArray[0], int(stringArray[1]))
        tasks.put(process)
    
    taskArray = [] # clearly an afterthought
    CPUTime = 0 #clock ticks
    while not tasks.empty(): # while have processes
        CPUTime += 1 #OVERHEAD for selecting a program (running dispatcher)
        process = tasks.get() # get next process on queue
        CPUTime += 3 #OVERHEAD for loading a process
        auditLog += ("{0:>5} {1:>10}: put on processor \n".format(CPUTime, process.name))
        CPUTime += process.time if process.time < TASK_TIME_LIMIT else TASK_TIME_LIMIT
        process.time -= TASK_TIME_LIMIT
        if process.time > 0: # if process is not done
            tasks.put(process) # put it back on the queue
            CPUTime += 3 #OVERHEAD for saving an incomplete process
            auditLog += "{1:>5} {0:>10}: Time left for process: {2:>5} \n".format(process.name, CPUTime, process.time)
        else:
            auditLog += "{1:>5} {0:>10}: complete \n".format(process.name, CPUTime)
            process.waitT = CPUTime - process.servT
            taskArray.append(process) # clearly an afterthought

    auditLog += ("Complete time is {0}\n".format(CPUTime))
    
#new...
    totTurnTime = 0 
    totNormTurnTime = 0
    for i in range(0, eleNum):
        totTurnTime += taskArray[i].waitT + taskArray[i].servT
        totNormTurnTime += (taskArray[i].waitT + taskArray[i].servT) / taskArray[i].servT
    auditLog += ("Average turnaround time is {0}\n".format(totTurnTime/eleNum))
    auditLog += ("Average normalized turnaround time is {0}\n".format(totNormTurnTime/eleNum))
#...new

    with open('auditLog.txt', 'w') as outFile: # output results
        outFile.write(auditLog)
