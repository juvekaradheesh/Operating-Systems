#####################################################
#
# PROGRAM - Priority Preemptive Scheduling
# AUTHOR  - Adheesh S. Juvekar
#
#####################################################

from __future__ import print_function
from random import randint

class Process:

    processCount = 0

    def __init__(self, pid, priority, timeArrival, timeBurst, timeRemaining, timeTurnAround, timeWaiting):
        self.pid = pid
        self.priority = priority
        self.timeArrival = timeArrival
        self.timeBurst = timeBurst
        self.timeRemaining = timeRemaining
        self.timeTurnAround = timeTurnAround
        self.timeWaiting = timeWaiting

        Process.processCount += 1

# Prcess enter processQueue after arrival
processQueue = []

# List of all processes
processes = []

# Used for displaying 
runArray = []
displayArray = []

# Put process in processQueue after its arrival
def putProcess():
    for process in processes:
        if process.timeArrival == i:
            processQueue.append(process.pid)
    return

# Return shortest process in processQueue
def getHighest():
    minVar = 11
    flag = False
    for i in processQueue:
        for process in processes:
            if i == process.pid:
                if process.priority < minVar and process.timeRemaining != 0:
                    minVar = process.priority
                    highestProcess = process
                    flag = True
    if flag:
        return highestProcess
    else:
        return Process(0, 0, 0, 0, 0, 0, 0)

#Decrement remaining time by 1
def run(p):
    p.timeTurnAround += 1
    p.timeRemaining = p.timeRemaining - 1
    for pq in processQueue:
        for process in processes:
            if process.pid == pq and process.timeRemaining > 0:
                if pq != p.pid:
                    process.timeTurnAround += 1
                    process.timeWaiting += 1


#Check if all processes are completed
def isDone():
    flag = True
    for processDone in processes:
        if processDone.timeRemaining > 0:
            flag = False
    return flag

# Declaring Processes in processes list
for i in range(5):
    time = randint(1, 10)
    processes.append(Process(i+1, randint(1, 5), randint(0, 10), time, time, 0, 0))

for process in processes:
    print("Process", process.pid, "Priority", process.priority, "TimeArrival", process.timeArrival, "TimeBurst", process.timeRemaining)

i = 0
while True:
    putProcess()
    highest = getHighest()
    run(highest)
    runArray.append(highest.pid)
    if highest.pid != 0:
        displayArray.append("P" + str(highest.pid))
    else:
        displayArray.append('_')
    i = i+1
    if isDone():
        break

print()
print("Gantt Chart")
index = 0
for i in displayArray:
    print(i + '|', sep=' ', end='', flush=True)
print()

timeTurnAround = 0
timeWaiting = 0
for process in processes:
    print(process.pid, process.timeWaiting, process.timeTurnAround)
    timeTurnAround += process.timeTurnAround
    timeWaiting += process.timeWaiting

print("Average Waiting Time =", timeWaiting/len(processes))
print("Average TurnAround Time =", timeTurnAround/len(processes))