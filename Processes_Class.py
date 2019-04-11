class Processes:
    # Process Name, Arrival Time, Burst Time, Priority
    Process_List = []
    # Process Name, Arrival Time, Finish Time, Waiting Time
    FCFS_List = []
    waiting_time = 0

    def addProcess(self, Name, Arrival_Time, Burst_Time, Priority):
        self.Process_List.append(
            {"task": Name, "arrival_time": Arrival_Time, "burst_time": Burst_Time, "priority": Priority})

    def FCFS(self):
        # Sort According to the Arrival Time
        self.Process_List.sort(key=lambda x: x["arrival_time"])
        # Implementation of FCFS List
        for i in range(len(self.Process_List)):
            # The First Process will have 0 Waiting Time
            if i == 0:
                self.FCFS_List.append(
                    {"Task": self.Process_List[0]["task"], "Start": self.Process_List[0]["arrival_time"],
                     "Finish": (self.Process_List[0]["burst_time"] + self.Process_List[0]["arrival_time"])})
            else:
                self.FCFS_List.append(
                    {"Task": self.Process_List[i]["task"], "Start": self.FCFS_List[i - 1]["Finish"],
                     "Finish": self.Process_List[i]["burst_time"] + self.FCFS_List[i - 1]
                     ["Finish"]})

                self.waiting_time += self.FCFS_List[i - 1]["Finish"] - self.Process_List[i]["arrival_time"]

        self.waiting_time /= len(self.Process_List)
        return self.FCFS_List, self.waiting_time

def FCFS(process):
    FCFS_List = []
    waiting_time=0
    # Sort According to the Arrival Time
    process.sort(key=lambda x: x["arrival_time"])
    # Implementation of FCFS List
    for i in range(len(process)):
        # The First Process will have 0 Waiting Time
        if i == 0:
            FCFS_List.append(
                {"Task": process[0]["task"], "Start": process[0]["arrival_time"],
                 "Finish": (process[0]["burst_time"] + process[0]["arrival_time"])})
        else:
            FCFS_List.append(
                {"Task": process[i]["task"], "Start": max([FCFS_List[i - 1]["Finish"], process[i]['arrival_time']]),
                 "Finish": process[i]["burst_time"] + FCFS_List[i - 1]
                 ["Finish"]})

            waiting_time += FCFS_List[i - 1]["Finish"] - process[i]["arrival_time"]

    waiting_time /= len(process)
    return FCFS_List, waiting_time

