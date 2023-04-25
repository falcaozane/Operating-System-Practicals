numberOfProcesses = int(input("Enter the number of Processes: "))
numberOfResources = int(input("Enter the number of Resource Instances: "))

available = list(map(int, input("Enter the Available Resources: ").split()))

allocation = []
print("\nEnter the Allocation Matrix:")
for i in range(numberOfProcesses):
    row = list(map(int, input("Process " + str(i) + ": ").split()))
    allocation.append(row)

request = []
print("\nEnter the Request Matrix:")
for i in range(numberOfProcesses):
    row = list(map(int, input("Process " + str(i) + ": ").split()))
    request.append(row)

# computing the need matrix
need = []
for i in range(numberOfProcesses):
    row = []
    for j in range(numberOfResources):
        row.append(request[i][j] - allocation[i][j])
    need.append(row)

# initializing the finish array with zeros
finish = [0] * numberOfProcesses

# detecting the deadlock
flag = True
while flag:
    flag = False
    for i in range(numberOfProcesses):
        if finish[i] == 0:
            c = 0
            for j in range(numberOfResources):
                if need[i][j] <= available[j]:
                    c += 1
                else:
                    break
            if c == numberOfResources:
                for k in range(numberOfResources):
                    available[k] += allocation[i][k]
                finish[i] = 1
                flag = True

# identifying the deadlocked processes
dead = []
for i in range(numberOfProcesses):
    if finish[i] == 0:
        dead.append(i)

# displaying the results
print("\nProcess\tAllocation\tRequest\t\tNeed\t\tFinish")
for i in range(numberOfProcesses):
    print("P" + str(i) + "\t", end="")
    print(allocation[i], end="\t\t")
    print(request[i], end="\t")
    print(need[i], end="\t")
    print(finish[i])
if len(dead) > 0:
    print("\nSystem is in Deadlock and the Deadlock process are:")
    for i in range(len(dead)):
        print("Process " + str(dead[i]))
else:
    print("\nNo Deadlock Detected")
