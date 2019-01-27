#####################################################
#
# PROGRAM - First Fit Algorithm
# AUTHOR  - Adheesh S. Juvekar
#
#####################################################
from __future__ import print_function

noOfBlocks = int(input("Enter number of blocks in memory : "))
noOfProcesses = int(input("Enter number of processes : "))

fragments = []
memoryAllocated = []
memoryBlocks = []
processes = []

print("Enter size of memory blocks")
for i in range(0, noOfBlocks):
    memoryBlocks.append(int(input("Block size of memory block " + str(i) + " : ")))
    memoryAllocated.append(-1)
    fragments.append(memoryBlocks[i])

print("Enter size of processes")
for i in range(0, noOfProcesses):
    processes.append(int(input("Size of Processes " + str(i) + " : ")))

for j in range(0,len(processes)):
    for i in range(0, noOfBlocks):
        if processes[j] <= memoryBlocks[i] and memoryAllocated[i] == -1:
            fragments[i] = memoryBlocks[i] - processes[j]
            memoryAllocated[i] = j
            break
        else:
            pass
    

print("Block Number   Block Size   Process Number   Process Size   Fragment")
for i in range(0, len(memoryBlocks)):
    print(str(i) + "         ", end = '')
    print("        " + str(memoryBlocks[i]) + "         ", end = '')
    print("        " + str(memoryAllocated[i]) if memoryAllocated[i] != -1 else "Not Allocated", end = '')
    print("          ", end='')
    print("     " + str(processes[memoryAllocated[i]]) if memoryAllocated[i] != -1 else "", end='')
    print("     ", end='')
    print("     " + str(fragments[i]) if memoryAllocated[i] != -1 else "")
