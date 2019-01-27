#####################################################
#
# PROGRAM - Page Replacement Algorithms
# AUTHOR  - Adheesh S. Juvekar
#
#####################################################

ph = 0
pf = 0

print("Enter number of frames : ")
noOfFrames = int(input())
print("Enter Pages : ")
pages = list(map(int, input().split()))

def fifo():
    for i in range(0, len(pages)):
        flag = False
        flag2 = False
        for j in range(0, len(frames)):
            if pages[i] == frames[j]:
                global ph
                ph += 1
                flag = True
                flag2 = True
        if not flag:
            if len(frames) < 3:
                frames.append(pages[i])
                global pf
                pf += 1
                flag2 = True
        if not flag2:
            sumM = 0
            maxI = -1
            for j in range(0, noOfFrames):
                if time[j] > sumM:
                    sumM = time[j]
                    maxI = j
            time[maxI] = -1
            frames[maxI] = pages[i]
            pf += 1

        for j in range(0, len(frames)):
                time[j] += 1


        # UNCOMMENT BELOW LINES TO SEE FRAMES ON EACH PAGE HIT/FAULT
        # print("\nframes : ")
        # for i in range(0, len(frames)):
        #     print(str(frames[i]) + " ", end='')

def lru():
    for i in range(0, len(pages)):
        flag = False
        flag2 = False
        for j in range(0, len(frames)):
            if pages[i] == frames[j]:
                time[j] = -1
                global ph
                ph += 1
                flag = True
                flag2 = True
        if not flag:
            if len(frames) < 3:
                frames.append(pages[i])
                global pf
                pf += 1
                flag2 = True
        if not flag2:
            sumM = 0
            maxI = -1
            for j in range(0, noOfFrames):
                if time[j] > sumM:
                    sumM = time[j]
                    maxI = j
            time[maxI] = -1
            frames[maxI] = pages[i]
            pf += 1

        for j in range(0, len(frames)):
                time[j] += 1


        # UNCOMMENT BELOW LINES TO SEE FRAMES ON EACH PAGE HIT/FAULT
        # print("\nframes : ")
        # for i in range(0, len(frames)):
        #     print(str(frames[i]) + " ", end='')

def lfu():
    for i in range(0, len(pages)):
        flag = False
        flag2 = False
        for j in range(0, len(frames)):
            if pages[i] == frames[j]:
                time[j] += 1
                global ph
                ph += 1
                flag = True
                flag2 = True
        if not flag:
            if len(frames) < 3:
                frames.append(pages[i])
                time[len(frames) - 1] = 1
                global pf
                pf += 1
                flag2 = True
        if not flag2:
            sumM = 99
            maxI = -1
            for j in range(0, noOfFrames):
                if time[j] < sumM:
                    sumM = time[j]
                    maxI = j
            time[maxI] = 1
            frames[maxI] = pages[i]
            pf += 1

        # UNCOMMENT BELOW LINES TO SEE FRAMES ON EACH PAGE HIT/FAULT
        # print("\nframes : ")
        # for i in range(0, len(frames)):
        #     print(str(frames[i]) + " ", end='')

def optimal():
    for i in range(0, len(pages)):
        flag = False
        flag2 = False
        for j in range(0, len(frames)):
            if pages[i] == frames[j]:
                global ph
                ph += 1
                flag = True
                flag2 = True
        if not flag:
            if len(frames) < 3:
                frames.append(pages[i])
                global pf
                pf += 1
                flag2 = True
        if not flag2:
            for j in range(0, len(frames)):
                time[j] = 99
            for j in range(0, len(frames)):
                for k in range(i, len(pages)):
                    if frames[j] == pages[k]:
                        time[j] = k - i
                        flag = True
                        break
            sumM = 0
            maxI = -1
            for j in range(0, len(frames)):
                if time[j] > sumM:
                    sumM = time[j]
                    maxI = j
            frames[maxI] = pages[i]
            pf += 1

        # UNCOMMENT BELOW LINES TO SEE FRAMES ON EACH PAGE HIT/FAULT
        # print("\nframes : ")
        # for i in range(0, len(frames)):
        #     print(str(frames[i]) + " ", end='')

while True:
    frames = []
    time = [-1]*3
    print("Select the memory allocation algorithm you want to use : ")
    print("1 : FIFO")
    print("2 : LRU")
    print("3 : LFU")
    print("4 : Optimal")
    print("5 : Exit")
    choice = input("Enter your choice : ")

    if choice == '1':
        fifo()
    elif choice == '2':
        lru()
    elif choice == '3':
        lfu()
    elif choice == '4':
        optimal()
    elif choice == '5':
        break
    else:
        print("Invalid input! please try again.")

    print("\npage hits =  " + str(ph))
    print("page faults = " + str(pf))
    ph = 0
    pf = 0

