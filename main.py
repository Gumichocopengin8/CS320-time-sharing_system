import queue


class Process:
    def __init__(self, name, processTime):
        self.name = name
        self.processTime = processTime


with open('test.txt','r') as file:
    ele = file.readline().split()
    eleNum = int(ele[0]) # number of process
    TASK_TIME_LIMIT = int(ele[1]) # quantum

    tasks = queue.Queue() # queue
    for i in range(0, eleNum):
        stringArray = file.readline().split()
        process = Process(stringArray[0], int(stringArray[1]))
        tasks.put(process)

    CPUTime = 0
    while tasks.qsize() > 0:
        process = tasks.get()
        CPUTime += TASK_TIME_LIMIT
        process.processTime -= TASK_TIME_LIMIT
        if process.processTime > 0:
            tasks.put(process)
            continue

        CPUTime += process.processTime
        print("{0} {1}".format(process.name, CPUTime))
