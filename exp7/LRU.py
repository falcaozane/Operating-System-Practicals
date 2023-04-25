def findLRU(time, n):
    minimum = time[0]
    pos = 0
    for i in range(1, n):
        if time[i] < minimum:
            minimum = time[i]
            pos = i
    return pos

no_of_frames = int(input("\nEnter the number of frames : "))
no_of_pages = int(input("\nEnter the number of pages : "))

frames = [-1] * no_of_frames
pages = []

print("\nEnter the Values of the Reference String : ")
for i in range(no_of_pages):
    pages.append(int(input("Value No. [%d] : " % (i+1))))

counter = 0
time = [0] * no_of_frames
faults = 0
for i in range(no_of_pages):
    flag1 = flag2 = 0
    for j in range(no_of_frames):
        if frames[j] == pages[i]:
            counter += 1
            time[j] = counter
            flag1 = flag2 = 1
            break
    if flag1 == 0:
        for j in range(no_of_frames):
            if frames[j] == -1:
                counter += 1
                faults += 1
                frames[j] = pages[i]
                time[j] = counter
                flag2 = 1
                break
    if flag2 == 0:
        pos = findLRU(time, no_of_frames)
        counter += 1
        faults += 1
        frames[pos] = pages[i]
        time[pos] = counter

    print("\n")
    for j in range(no_of_frames):
        print(" %d\t" % frames[j], end="")

page_hits = no_of_pages - faults
print("\n Total Page Hits : %d" % page_hits)
print("\n Total Page Miss : %d" % faults)
print("\n Page Hit Ratio : %f" % (float(page_hits) / no_of_pages))
print("\n Page Miss Ratio : %f" % (float(faults) / no_of_pages))
