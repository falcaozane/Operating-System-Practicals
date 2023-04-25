# CPU Scheduling - Round Robin

n = int(input("Enter Number of Processes: "))

p = []  # list of processes

# get process information from user input
for i in range(n):
    name = chr(65 + i)  # generate process name (A, B, C, ...)
    print("\nProcess", name)
    at = int(input("Arrival Time: "))
    bt = int(input("Burst Time: "))
    p.append({"name": name, "at": at, "bt": bt, "rt": bt, "completed": False})
    
tq = int(input("\nEnter the time quantum: "))

p.sort(key=lambda x: x["at"])  # sort processes by arrival time

queue = [0]  # initialize queue with first process
time = p[0]["at"]  # initialize time with first process arrival time

print("Process execution order: ", end="")

# run until all processes have completed
while any(not p[i]["completed"] for i in range(n)):
    i = queue.pop(0)  # get next process from queue
    if p[i]["rt"] <= tq:  # process completes
        time += p[i]["rt"]
        p[i]["rt"] = 0
        p[i]["completed"] = True
        print(p[i]["name"], end=" ")
        p[i]["wt"] = time - p[i]["at"] - p[i]["bt"]
        p[i]["tt"] = time - p[i]["at"]
        for j in range(n):  # enqueue new processes
            if not p[j]["completed"] and p[j]["at"] <= time and j not in queue:
                queue.append(j)
    else:  # process not completed
        time += tq
        p[i]["rt"] -= tq
        print(p[i]["name"], end=" ")
        for j in range(n):  # enqueue new processes
            if not p[j]["completed"] and p[j]["at"] <= time and j != i and j not in queue:
                queue.append(j)
        queue.append(i)  # enqueue uncompleted process

# calculate average waiting time and turnaround time
avg_wt = sum(p[i]["wt"] for i in range(n)) / n
avg_tt = sum(p[i]["tt"] for i in range(n)) / n

# print process information
print("\nName\tArrival Time\tBurst Time\tResponse Time\tTurnaround Time")
for i in range(n):
    print("{}\t\t{}\t\t{}\t\t{}\t\t{}".format(
        p[i]["name"], p[i]["at"], p[i]["bt"], p[i]["wt"], p[i]["tt"]))

# print average waiting time and turnaround time
print("\nAverage waiting time: {:.2f}".format(avg_wt))
print("Average turnaround time: {:.2f}".format(avg_tt))
