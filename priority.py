def priority_scheduling(processes, preemptive):
    output = []
    waiting_time = 0
    total = len(processes)
    if not preemptive:
        current_time = 0
        while len(processes) > 0:
            current = minimum_arrival_time(processes, current_time)
            if len(current) == 0:
                current_time += 1
                continue
            process = schedule(current, output, preemptive, 0)
            waiting_time += (current_time - process["arrival_time"])
            output.append(process)
            current_time += process["burst_time"]
            processes.remove(process)
    else:
        current_time = 0
        waiting_time -= sum(x['burst_time'] for x in processes)
        current_process = {}
        while len(processes) != 0:
            if bool(current_process) and processes[processes.index(current_process)]["burst_time"] == 0:
                waiting_time += (current_time -
                                 current_process["arrival_time"])
                processes.remove(current_process)
            if len(processes) == 0:
                break
            current_process = schedule(
                processes, output, preemptive, current_time)
            if current_process == {}:
                current_time += 1
                output.append(current_process)
                continue

            output.append(current_process)
            processes[processes.index(current_process)]["burst_time"] -= 1
            current_time += 1

    print(output)
    output = reshape_output(output, preemptive)

    return [output, waiting_time / total]


def schedule(in_list, output, preemptive, current_time):
    temp = []
    if not preemptive:
        temp = in_list
        temp.sort(key=priority_sorting)
        temp.reverse()
        next = temp.pop()

    else:
        for process in in_list:
            if process["arrival_time"] <= current_time:
                temp.append(process)
        if len(temp) == 0:
            return {}

        temp.sort(key=priority_sorting)
        temp.reverse()
        next = temp.pop()

    return next


def minimum_arrival_time(processes, time):
    output = []
    for process in processes:
        if process["arrival_time"] <= time:
            output.append(process)
    return output


def priority_sorting(element):
    return element["priority"]


def reshape_output(scheduled_processes, preemptive):
    gantt = []
    if preemptive:
        flag = False
        for process in scheduled_processes:
            if process == {}:
                flag = True
                continue

            if len(gantt) != 0 and gantt[-1]["Task"] != process["task"]:
                gantt.append(
                    {"Task": process["task"], "Start": process['arrival_time'] if flag else gantt[-1]['Finish'], "Finish": gantt[-1]['Finish'] + 1})

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
                    {"Task": process["task"], "Start": max([process['arrival_time'], gantt[-1]['Finish']]),
                     "Finish": max([process['arrival_time'], gantt[-1]['Finish']]) + process['burst_time']})
    return gantt
