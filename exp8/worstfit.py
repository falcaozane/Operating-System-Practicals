blocks = [100, 500, 200, 300, 600]
process = [212, 417, 112, 426, 80, 2, 900]
m = len(blocks)
n = len(process)
allocation = [-1]*n
print('memory allocation')
for i in range(n):
    index = -1
    worst = min(blocks)
    for j in range(m):
        if blocks[j]>=process[i]:
            if blocks[j]>worst:  # fixed the comparison operator
                worst = blocks[j]
                index = j
    if index != -1:  # fixed the condition
        allocation[i]=worst
        blocks[index] -= process[i]
    print('memory blocks after ',i+1,' process -->',blocks)

print()
print("Process No.      Process Size            Block")
for i in range(n):
    print('       ',i + 1, "              ", process[i],end = "\t\t\t")
    if allocation[i] != -1:
        print(allocation[i])
    else:
        print("Not Allocated")
