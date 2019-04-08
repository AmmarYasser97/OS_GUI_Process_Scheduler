from roundRobin import round_robin

p = [{'arrival_time': 0, 'task': "0", "burst_time": 10}, {'arrival_time': 1, 'task': "1", "burst_time": 10},
     {'arrival_time': 2, 'task': "2", "burst_time": 7}]

out = round_robin(p, 3)
for x in out[0]:
    print(x)

print(out[1])
