import queue


class Process:

    def __init__(self, name, processTime):
        self.name = name
        self.processTime = processTime
        

with open('test.txt','r') as file:
    ele = file.readline().split()
    eleNum = int(ele[0])
    quantum = int(ele[1])

    que = queue.Queue() 
    for i in range(0, eleNum):
        stringArray = file.readline().split()
        process = Process(stringArray[0], int(stringArray[1]))
        que.put(process)

    CPUTime = 0
    while que.qsize() > 0:
        process = que.get()
        CPUTime += quantum
        process.processTime -= quantum
        if process.processTime > 0:
            que.put(process)
            continue

        CPUTime += process.processTime
        print("{0} {1}".format(process.name, CPUTime))
