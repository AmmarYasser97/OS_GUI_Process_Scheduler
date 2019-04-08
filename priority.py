def priority_scheduling(processes, preemptive):
    output = []
    waiting_time = 0
    total = len(processes)
    if not preemptive:
        current_time = 0
        while len(processes) > 0:
            current = minimum_arrival_time(processes)
            process = schedule(current, output, preemptive, 0)
            waiting_time += (current_time - process["arrival_time"])
            output.append(process)
            current_time += process["burst_time"]
            processes.remove(process)
    else:
        waiting_time -= sum(x['burst_time'] for x in processes)
        current_process = {}
        for current_time in range(
                sum(x['burst_time'] for x in processes) + min(x['arrival_time'] for x in processes) + 1):
            if bool(current_process) and processes[processes.index(current_process)]["burst_time"] == 0:
                waiting_time += (current_time -
                                 current_process["arrival_time"])
                processes.remove(current_process)
            if len(processes) == 0:
                break
            current_process = schedule(
                processes, output, preemptive, current_time)
            output.append(current_process)
            processes[processes.index(current_process)]["burst_time"] -= 1

    output = reshape_output(output, preemptive)

    return [output, waiting_time / total]


def schedule(in_list, output, preemptive, current_time):
    temp = []
    if not preemptive:
        for process in in_list:
            if process["arrival_time"] <= (sum(x['burst_time'] for x in output)):
                temp.append(process)

        temp.sort(key=priority_sorting)
        temp.reverse()
        next = temp.pop()
        in_list.remove(next)

    else:
        for process in in_list:
            if process["arrival_time"] <= current_time:
                temp.append(process)
        temp.sort(key=priority_sorting)
        temp.reverse()
        next = temp.pop()

    return next


def minimum_arrival_time(processes):
    minimum = processes[0]["arrival_time"]
    output = []
    for process in processes:
        if process["arrival_time"] <= minimum:
            output.append(process)
    return output


def priority_sorting(element):
    return element["priority"]


def reshape_output(scheduled_processes, preemptive):
    gantt = []
    if preemptive:
        for process in scheduled_processes:
            if len(gantt) != 0 and gantt[-1]["Task"] != process["task"]:
                gantt.append({"Task": process["task"], "Start": gantt[-1]['Finish'], "Finish": gantt[-1]['Finish'] + 1})

            elif len(gantt) == 0:
                gantt.append(
                    {"Task": process["task"], "Start": process['arrival_time'], "Finish": process['arrival_time'] + 1})
            else:
                gantt[-1]["Finish"] += 1

    else:
        for process in scheduled_processes:
            if len(gantt) == 0:
                gantt.append(
                    {"Task": process["task"], "Start": process['arrival_time'],
                     "Finish": process['arrival_time'] + process['burst_time']})
            else:
                gantt.append(
                    {"Task": process["task"], "Start": gantt[-1]['Finish'],
                     "Finish": gantt[-1]['Finish'] + process['burst_time']})
    return gantt
