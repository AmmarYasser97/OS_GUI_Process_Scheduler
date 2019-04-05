from Process import *
def sortKey(x):
    return id(x)
def roundRobin(processes, quantum ):
    time=0
    i=0
    output= []
    while len(processes)>0:
        if (processes[i].arrival_time>time):
            i = (i+1) % len(processes)
            time+=1
            continue
        if (processes[i].burst_done < quantum):
            processes[i].burst_done += quantum
            time += quantum
            i = (i+1) % len(processes)
        else:
            time+= processes[i].duration - processes[i].burst_done
            processes[i].end_time=time
            processes[i].waiting_time = processes[i].end_time - processes[i].arrival_time - processes[i].duration
            output.append(processes[i])
            processes.pop(i)
            if len(processes)==0:
                break
            i= (i-1)% len(processes)
    output.sort(key=sortKey)
    
    return output
