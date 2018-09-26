import queue


class Process:
    def __init__(self, name, time):
        self.name = name
        self.time = time


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
        print("{0} \t{1} put on processor.".format(CPUTime, process.name))
        CPUTime += process.time if process.time < TASK_TIME_LIMIT else TASK_TIME_LIMIT
        process.time -= TASK_TIME_LIMIT
        if process.time > 0: # if process is not done
            tasks.put(process) # put it back on the queue
            CPUTime += 3 #OVERHEAD for saving an incomplete process
            print("{0} \t{1} removed from the processor.".format(CPUTime, process.name) + " Time left for process: {0}".format(process.time))
        else:
            print("{0} \t{1} removed from the processor.".format(CPUTime, process.name) + " {0} is complete.".format(process.name))

    print("Complete time is {0}".format(CPUTime))
