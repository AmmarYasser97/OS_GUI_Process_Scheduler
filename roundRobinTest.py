from roundRobin import round_robin

p = [{'arrival_time': 0, 'task': "0", "burst_time": 3}, {'arrival_time': 5, 'task': "1", "burst_time": 2},
     {'arrival_time': 9, 'task': "2", "burst_time": 6}]

out = round_robin(p, 2)
for x in out[0]:
    print(x)

print(out[1])
