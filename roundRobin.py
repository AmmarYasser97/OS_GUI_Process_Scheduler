class Process:
    pid = ""
    arrival_time = 0
    end_time = 0
    duration = 0
    burst_done = 0
    waiting_time = 0

    def __init__(self, x, y, z):
        self.arrival_time = x
        self.duration = y
        self.pid = z

    def printProcess(self):
        print("arrival time:", self.arrival_time, "end time:", self.end_time, "waiting time:", self.waiting_time,
              "duration:", self.duration)


def sortKey(x):
    return x.pid


def round_robin(prc, quantum):
    processes = []
    for x in prc:
        processes.append(Process(x['arrival_time'], x['burst_time'], x['task']))
    time = 0
    i = 0
    output = []
    outdict = []
    while len(processes) > 0:
        if (processes[i].arrival_time > time) and len(processes) == 1:
            i = (i + 1) % len(processes)
            time += 1
            continue
        elif processes[i].arrival_time > time:
            i = (i + 1) % len(processes)

        if processes[i].duration - processes[i].burst_done > quantum:
            processes[i].burst_done += quantum
            time += quantum
            if len(outdict) > 0:
                if outdict[-1]['Task'] == processes[i].pid:
                    outdict[-1]['Finish'] += processes[i].duration - processes[i].burst_done
                else:
                    outdict.append({"Task": processes[i].pid, "Start": time - quantum, "Finish": time})
                    i = (i + 1) % len(processes)
            else:
                outdict.append({"Task": processes[i].pid, "Start": time - quantum, "Finish": time})
                i = (i + 1) % len(processes)
        else:
            if len(outdict) > 0:

                if outdict[-1]['Task'] == processes[i].pid:
                    outdict[-1]['Finish'] += processes[i].duration - processes[i].burst_done
                else:
                    outdict.append({"Task": processes[i].pid, "Start": time,
                                    "Finish": time + processes[i].duration - processes[i].burst_done})
            else:
                outdict.append({"Task": processes[i].pid, "Start": time,
                                "Finish": time + processes[i].duration - processes[i].burst_done})
            time += processes[i].duration - processes[i].burst_done
            processes[i].end_time = time
            processes[i].waiting_time = processes[i].end_time - processes[i].arrival_time - processes[i].duration

            output.append(processes[i])
            processes.pop(i)
            if len(processes) == 0:
                break
            i = i % len(processes)
    output.sort(key=sortKey)

    return outdict, sum(x.waiting_time for x in output) / len(output)
