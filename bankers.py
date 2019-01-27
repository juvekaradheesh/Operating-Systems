#####################################################
#
# PROGRAM - Banker's Algorithm
# AUTHOR  - Adheesh S. Juvekar
#
#####################################################
from __future__ import print_function
import copy


Allocation = [[0, 0, 1, 2], [1, 0, 0, 0], [1, 3, 5, 4], [0, 6, 3, 2], [0, 0, 1, 4]]
Max = [[0, 0, 1, 2], [1, 7, 5, 0], [2, 3, 5, 6], [0, 6, 5, 2], [1, 6, 5, 6]]
Finish = [False, False, False, False, False]
Available = [1, 5, 2, 0]


resourceAvailable = []
complete = []
allocated = [[], [], [], [], []]
maxAllocated = [[], [], [], [], []]
order = []
need = [[], [], [], [], []]

def copyData():
    global resourceAvailable
    resourceAvailable = copy.deepcopy(Available)
    global allocated
    allocated = copy.deepcopy(Allocation)
    global maxAllocated
    maxAllocated = copy.deepcopy(Max)
    global complete
    complete = copy.deepcopy(Finish)
    global need
    need = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    global order
    order = []


    # Calculate Need Matrix
    for i in range(0, 5):
        for j in range(0, 3):
            need[i][j] = maxAllocated[i][j] - allocated[i][j]
    
    return

# Copy Data for calculation
copyData()

# Display Given Processes
for i in range(0, 5):
    print("*****************")
    print("Process ", i + 1, " :")
    print("Allocated : ")
    for j in range(0, 4):
        print(str(allocated[i][j]) + ' ', sep = ' ', end = '', flush = True)
    print()
    print("Max Allocation : ")
    for j in range(0, 4):
        print(str(maxAllocated[i][j]) + ' ', sep = ' ', end = '', flush = True)
    print()
    print("Calculated Need : ")
    for j in range(0, 4):
        print(str(need[i][j]) + ' ', sep = ' ', end = '', flush = True)
    print()

def safetyTest():
    while True:
        safe = False
        running = False
        completed = True

        for i in range(0, 5):
            if complete[i]:
                continue
            completed = False
            availFlag = True
            for j in range(0, 4):
                if need[i][j] > resourceAvailable[j]:
                    availFlag = False
                    break
            if availFlag:
                running = True
                for j in range(0, 4):
                    resourceAvailable[j] += allocated[i][j]
                    need[i][j] = 0
                    allocated[i][j] = 0

                order.append(i)
                complete[i] = True

        if completed:
            safe = True
            break

        if running == False:
            safe = False
            break


    print()
    if safe:
        print("This System is in Safe state")
        return True
    else:
        print("This System is not in Safe state")
        return False


# Run Safety Test
safetyTest()

print("\nNew process request for process P1 with request need 0 4 2 0 for A B C D respectively")
request = [0, 4, 2, 0]

def resourceRequest():
    
    # Copy data for calculation
    copyData()

    # Check if request is less than need
    for i in range(0, len(request)):
        if request[i] > need[1][i]:
            print("\nRequest is more that the need, thus request cannot be granted")
            return
    flag = True
    for i in range(0, len(request)):
        if request[i] > resourceAvailable[i]:
            flag = False
            break
    if flag:
        for i in range(0, len(resourceAvailable)):
            resourceAvailable[i] = resourceAvailable[i] - request[i]

        for i in range(0, len(request)):
            allocated[1][i] = allocated[1][i] + request[i]

        for i in range(0, len(request)):
            need[1][i] = need[1][i] - request[i]
    if safetyTest():
        print("\nRequest can be granted")
    else:
        print("\nRequest cannot be granted")

# Resource Request
resourceRequest()