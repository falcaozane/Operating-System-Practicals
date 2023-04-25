processes = [
    {'name': 'P1', 'priority': 3, 'burst_time': 10},
    {'name': 'P2', 'priority': 1, 'burst_time': 6},
    {'name': 'P3', 'priority': 4, 'burst_time': 8},
    {'name': 'P4', 'priority': 2, 'burst_time': 3},
]

# sort processes by priority (higher priority first)
processes = sorted(processes, key=lambda p: p['priority'], reverse=True)

completion_time = [0] * len(processes)
turnaround_time = [0] * len(processes)
waiting_time = [0] * len(processes)

for i, process in enumerate(processes):
    if i == 0:
        completion_time[i] = process['burst_time']
    else:
        completion_time[i] = completion_time[i-1] + process['burst_time']
    turnaround_time[i] = completion_time[i]
    waiting_time[i] = turnaround_time[i] - process['burst_time']

# print results
print("Process\tPriority\tBurst Time\tCompletion Time\tTurnaround Time\tWaiting Time")
for i, process in enumerate(processes):
    print(f"{process['name']}\t\t{process['priority']}\t\t{process['burst_time']}\t\t{completion_time[i]}\t\t{turnaround_time[i]}\t\t{waiting_time[i]}")
    
average_waiting_time = sum(waiting_time) / len(processes)
average_turnaround_time = sum(turnaround_time) / len(processes)
print(f"Average Waiting Time: {average_waiting_time}")
print(f"Average Turnaround Time: {average_turnaround_time}")
