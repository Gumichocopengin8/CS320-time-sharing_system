# Keita Nonaka # CTO coding leader
# Nick Smith # CEO
# Kyle Wyse # COO
# Koki Omori # CFO
# 30 Sep 2018
# Updated 6 Dec 2018
# OS Simulation

# This program Simulates a Time Sharing Operating System
# It takes an input file 'input.txt.' to run and produce an output file named 'auditLog.txt'. The format of the input file should be as follows:
# <number of tasks> <CPU time limit> !!! code no longer uses this but has not been changed to account for that. therefore there are "dummy" values in the input file
# <job1 name> <job1 total time>
# <jobN name> <jobN total time>

import queue

class Process:
    def __init__(self, name, time):
        self.name = name
        self.time = self.servT = time
        self.waitT = 0

with open('test.txt','r') as file, open('auditLog.txt','w') as outFile:
    auditLog = '{0:>5} {1:>10} {2:>5} \n\n'.format('Time', 'PID', 'log') # for output.txt file
    CPUTime = totTurnTime = totNormTurnTime = 0 
    tasks = queue.PriorityQueue()
    data = []
    eleNum = int(file.readline().split()[0]) # number of process

    for _ in range(eleNum):
        stringArray = file.readline().split()
        tasks.put([int(stringArray[1]), Process(stringArray[0], int(stringArray[1]))])

    while not tasks.empty(): # while have processes
        CPUTime += 1 #OVERHEAD for selecting a program (running dispatcher)
        process = tasks.get()[1] # get next process on queue
        data += [process]
        CPUTime += 3 #OVERHEAD for loading a process
        auditLog += ("{0:>5} {1:>10}: put on processor\n".format(CPUTime, process.name))
        process.waitT = CPUTime
        CPUTime += process.time
        auditLog += "{1:>5} {0:>10}: complete\n".format(process.name, CPUTime)
    auditLog += ("Complete time is {0}\n".format(CPUTime))

    for item in data:
        totTurnTime += item.waitT + item.servT
        totNormTurnTime += (item.waitT + item.servT) / item.servT
    auditLog += ("Average turnaround time is {0}\n".format(totTurnTime/len(data)))
    auditLog += ("Average normalized turnaround time is {0}\n".format(totNormTurnTime/len(data)))
    outFile.write(auditLog)
