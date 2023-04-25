from collections import deque

class Process:
    def __init__(self, name, arrival_time, burst_time):
        self.name = name
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.waiting_time = 0
        self.turnaround_time = 0

def round_robin(processes, quantum):
    queue = deque()
    current_time = 0
    total_waiting_time = 0
    total_turnaround_time = 0
    completed_processes = []

    for process in processes:
        queue.append(process)

    while queue:
        current_process = queue.popleft()
        if current_process.remaining_time <= quantum:
            current_time += current_process.remaining_time
            current_process.turnaround_time = current_time - current_process.arrival_time
            current_process.waiting_time = current_process.turnaround_time - current_process.burst_time
            total_waiting_time += current_process.waiting_time
            total_turnaround_time += current_process.turnaround_time
            completed_processes.append(current_process)
        else:
            current_time += quantum
            current_process.remaining_time -= quantum
            while queue and queue[-1] == current_process:
                queue.pop()
            queue.append(current_process)

    print("Name\tArrival Time\tBurst Time\tWaiting Time\tTurnaround Time")
    for process in completed_processes:
        print(f"{process.name}\t{process.arrival_time}\t\t{process.burst_time}\t\t{process.waiting_time}\t\t{process.turnaround_time}")

    avg_waiting_time = total_waiting_time / len(completed_processes)
    avg_turnaround_time = total_turnaround_time / len(completed_processes)
    print(f"Average waiting time: {avg_waiting_time}")
    print(f"Average turnaround time: {avg_turnaround_time}")

if __name__ == "__main__":
    processes = [
        Process('A', 0, 5),
        Process('B', 1, 3),
        Process('C', 2, 8),
        Process('D', 3, 6)
    ]
    quantum = 2

    round_robin(processes, quantum)
