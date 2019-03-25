class Processes:
    # Process Name, Arrival Time, Burst Time, Priority
    Process_List = [[]]
    # Process Name, Arrival Time, Finish Time, Waiting Time
    FCFS_List = [[]]

    def addProcess(Name, Arrival_Time, Burst_Time, Priority):
        Process_List.append(Name, Arrival_Time, Burst_Time, Priority)

    def FCFS():
        # Sort According to the Arrival Time
        Process_List.sort(key=lambda x: x[1])
        # Implementation of FCFS List
        for i in range(len(Process_List)):
            # The First Process will have 0 Waiting Time
            if(i == 0):
                FCFS_List.append(
                    Process_List[0][0], Process_List[0][1], Process_List[0][2], 0)
            else:
                FCFS_List.append(Process_List[i][0], Process_List[i][1], Process_List[i][2]+FCFS_List[i-1]
                                 [2], (Process_List[i][1])+(Process_List[i][2])-(Process_List[i][2]+FCFS_List[i-1][2]))
        return FCFS_List
