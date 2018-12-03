# Keita Nonaka # CTO coding leader
# Nick Smith # CEO
# Kyle Wyse # COO
# Koki Omori # CFO
# 30 Sep 2018
# Updated 29 Nov 2018
# OS Simulation

# This program Simulates a Time Sharing Operating System
# It takes an input file 'input.txt.' to run. The format of the input file should be as follows:
# <number of tasks> <CPU time limit> !!! code no longer uses this but has not been changed to account for that. therefore there are "dummy" values in the input file
# <job1 name> <job1 total time>
# <jobN name> <jobN total time>
# It will also provide an output file named 'auditLog.txt'

import queue

class Process:
    def __init__(self, name, time):
        self.name = name
        self.time = time
        self.waitT = 0 # new
        self.servT = time #new

with open('test.txt','r') as file: # read file
    auditLog = '{0:>5} {1:>10} {2:>5} \n\n'.format('Time', 'PID', 'log') # for output.txt file
    data = []
    tasks = queue.Queue()
    ele = file.readline().split()
    eleNum = int(ele[0]) # number of process
    TASK_TIME_LIMIT = int(ele[1])

    for i in range(eleNum):
        stringArray = file.readline().split()
        data += [Process(stringArray[0], int(stringArray[1]))]
    data = sorted(data, key=lambda love: love.time)

    for i in range(len(data)):
        tasks.put(data[i])

    CPUTime = 0 #clock ticks
    while not tasks.empty(): # while have processes
        CPUTime += 1 #OVERHEAD for selecting a program (running dispatcher)
        process = tasks.get() # get next process on queue
        CPUTime += 3 #OVERHEAD for loading a process
        auditLog += ("{0:>5} {1:>10}: put on processor\n".format(CPUTime, process.name))
        process.waitT = CPUTime #new
        CPUTime += process.time
        process.time -= TASK_TIME_LIMIT # is this line still necessary...?
        auditLog += "{1:>5} {0:>10}: complete\n".format(process.name, CPUTime)
    auditLog += ("Complete time is {0}\n".format(CPUTime))

#new...
    totTurnTime = 0 
    totNormTurnTime = 0
    for i in range(len(data)):
        totTurnTime += data[i].waitT + data[i].servT
        totNormTurnTime += (data[i].waitT + data[i].servT) / data[i].servT
    auditLog += ("Average turnaround time is {0}\n".format(totTurnTime/len(data)))
    auditLog += ("Average normalized turnaround time is {0}\n".format(totNormTurnTime/len(data)))
#...new

    with open('auditLog.txt', 'w') as outFile: # output results
        outFile.write(auditLog)
