import queue


class Process:
    def __init__(self, name, time):
        self.name = name
        self.time = time


with open('test.txt','r') as file:
    ele = file.readline().split()
    eleNum = int(ele[0]) # number of process
    TASK_TIME_LIMIT = int(ele[1]) # quantum
    
    #add all the processes to the tasks queue
    tasks = queue.Queue() # queue
    for i in range(0, eleNum):
        stringArray = file.readline().split()
        process = Process(stringArray[0], int(stringArray[1]))
        tasks.put(process)
    #
    CPUTime = 0 #clock ticks
    while not tasks.empty(): # while have processes
        process = tasks.get() # get next process on queue
        # run it for 40 ticks
        if(process.time < TASK_TIME_LIMIT):
            CPUTime += process.time
        else:
            CPUTime += TASK_TIME_LIMIT
        process.time -= TASK_TIME_LIMIT
        
        if process.time > 0: # if process is not done
            tasks.put(process) # put it pack on the queue
            #continue

        #CPUTime += process.time
        print("{0} {1}".format(process.name, CPUTime))
