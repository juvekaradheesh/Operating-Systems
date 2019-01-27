#####################################################
#
# PROGRAM - Memory Allocation Algorithms
# AUTHOR  - Adheesh S. Juvekar
#
#####################################################

while(True):
    
    print("****MENU****")
    print("1 : FCFS")
    print("2 : SSTF")
    print("3 : Exit")
    choice = int(input())

    if choice == 3:
        break

    print("Enter range from 0 to : ")
    rangeOf = int(input())
    print("Current pointer at : ")
    ptr = int(input())
    print("Enter the queue requests : ")
    reqQueue = list(map(int, input().split()))
    totHeadMov = 0
    
    if choice == 1:
        for i in range(0, len(reqQueue)):
            totHeadMov += abs(reqQueue[i] - ptr)
            ptr = reqQueue[i]

    elif choice == 2:
        for i in range(0, len(reqQueue)):
            min = 99999
            minI = 0
            for i in range(0, len(reqQueue)):
                if abs(reqQueue[i] - ptr) < min:
                    min = abs(reqQueue[i] - ptr)
                    minI = i
            ptr = reqQueue[minI]
            reqQueue[minI] = 99999
            totHeadMov += min
    
    else:
        print("Enter Valid Input")
        continue

    print("Total Head Movements : "+ str(totHeadMov))
