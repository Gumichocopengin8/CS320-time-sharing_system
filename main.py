import queue


class Process:
    def __init__(self, name, time):
        self.name = name
        self.time = time

output = ''

with open('test.txt','r') as file:
    ele = file.readline().split()
    eleNum = int(ele[0]) # number of process
    TASK_TIME_LIMIT = int(ele[1]) # quantum

    tasks = queue.Queue() # queue
    for i in range(0, eleNum): #add all the processes to the tasks queue
        stringArray = file.readline().split()
        process = Process(stringArray[0], int(stringArray[1]))
        tasks.put(process)

    CPUTime = 0
    while not tasks.empty(): # while have processes
        process = tasks.get()
        CPUTime += process.time if process.time < TASK_TIME_LIMIT else TASK_TIME_LIMIT
        process.time -= TASK_TIME_LIMIT
        if process.time > 0:
            tasks.put(process)
            output += "{0:<5} {1:>10}: Time left for process: {2:>5} \n".format(process.name, CPUTime, process.time)
            print("{0:<5} {1:>10}: Time left for process: {2:>5}".format(process.name, CPUTime, process.time))
        else:
            output += "{0:<5} {1:>10}: {2:<5} is complete \n".format(process.name, CPUTime, process.name)
            print("{0:<5} {1:>10}: {2:<5} is complete".format(process.name, CPUTime, process.name))
    print("Complete time is {0}".format(CPUTime))

with open('output.txt', 'a') as outFile:
    # outFile.del('') # i will fix it 
    outFile.write(output)
