def findMin(diff):
    index = -1
    minimum = 999999999
    for i in range(len(diff)):
        if (not diff[i][1] and
                minimum > diff[i][0]):
            minimum = diff[i][0]
            index = i
    return index
def SSTF(request, head):            
    if (len(request) == 0):
        return
    l = len(request)
    diff = [0] * l
    for i in range(l):
        diff[i] = [0, 0] 
    seek_count = 0
    seek_sequence = [0] * (l + 1)
    for i in range(l):
        seek_sequence[i] = head
        for i in range(len(diff)):
            diff[i][0] = abs(request[i] - head)
        index = findMin(diff)
        diff[index][1] = True
        seek_count += diff[index][0]
        head = request[index]
    seek_sequence[len(seek_sequence) - 1] = head
    print("Seek Sequence is")
    print(seek_sequence[0],end=" ")
    for i in range(1,l + 1):
        print(" ==> ",seek_sequence[i],end=" ")
    return seek_count

if __name__ == "__main__":
    Number_disk = int(input("Enter the number of disks: "))
    if Number_disk > 0:
        head = int(input("Enter initial header position: "))
        while not head in range(Number_disk + 1):
            head = int(input("Please enter valid initial head position: "))
        sequence = []
        sequence = list(map(int, input("Enter the sequence:").split()))
        for i in sequence:
            if i < 0 or i >= Number_disk:
                print("Sequence out of range")
                exit(0)

        seek_operations = SSTF(sequence, head)
        print("\nSeek Time: ", seek_operations)
