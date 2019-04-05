class Process:
    arrival_time=0
    end_time=0
    duration=0
    burst_done=0
    waiting_time = 0
    def __init__(self,x,y):
        self.arrival_time=x
        self.duration=y
    def printProcess(self):
        print("arrival time:",self.arrival_time,"end time:",self.end_time , "waiting time:", self.waiting_time,"duration:",self.duration)
