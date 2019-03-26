def priority_scheduling(processes, preemptive):
    output = []
    if not preemptive:
        while len(processes) > 0:
            current = minimum_arrive_time(processes)
            process = schedule(current, output, preemptive, 0)
            output.append(process)
            processes.remove(process)
    else:
        current_process = {}
        for current_time in range(sum(x['burst_time'] for x in processes)):
            current_process = schedule(
                processes, output, preemptive, current_time)
            output.append(current_process)
            processes[processes.index(current_process)]["burst_time"] -= 1
            if processes[processes.index(current_process)]["burst_time"] == 0:
                processes.remove(current_process)
                current_process = {}

    return output


def schedule(in_list, output, preemptive, current_time):
    temp = []
    if not preemptive:
        for process in in_list:
            if process["arrive_time"] <= (sum(x['burst_time'] for x in output)):
                temp.append(process)

        temp.sort(key=priority_sorting)
        temp.reverse()
        next = temp.pop()
        in_list.remove(next)

    else:
        for process in in_list:
            if process["arrive_time"] <= current_time:
                temp.append(process)
        temp.sort(key=priority_sorting)
        temp.reverse()
        next = temp.pop()

    return next


def minimum_arrive_time(processes):
    minimum = processes[0]["arrive_time"]
    output = []
    for process in processes:
        if process["arrive_time"] <= minimum:
            output.append(process)
    return output


def priority_sorting(element):
    return element["priority"]


task0 = {
    "id": 0,
    "arrive_time": 1,
    "burst_time": 3,
    "priority": 0,
}

task1 = {
    "id": 1,
    "arrive_time": 0,
    "burst_time": 2,
    "priority": 1,
}

task2 = {
    "id": 2,
    "arrive_time": 1,
    "burst_time": 1,
    "priority": 2,
}

scheduled = priority_scheduling([task0, task1, task2], True)
for x in scheduled:
    print(x)
