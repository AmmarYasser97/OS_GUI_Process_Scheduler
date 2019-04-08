from roundRobin import *

p = [{'arrival_time': 0, 'task': "0", "burst_time": 5}, {'arrival_time': 30, 'task': "1", "burst_time": 9},
     {'arrival_time': 2, 'task': "2", "burst_time": 7}, {'arrival_time': 2, 'task': "3", "burst_time": 5},
     {'arrival_time': 4, 'task': "4", "burst_time": 6}]

out = round_robin(p, 4)
for x in out[0]:
    print(x)

print(out[1])
