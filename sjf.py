def average(lst):
    return sum(lst) / len(lst)


def sjf(input_list, is_preemptive=False):
    output_list = []
    waiting_time = []
    start_time = []
    input_list = sorted(input_list, key=lambda k: (k['arrival_time'], k['burst_time']))

    if is_preemptive:
        end_time = []
        arrived_tasks = []
        current_time = 0
        done_processes = 0
        ready_processes = 0

        while done_processes < len(input_list):
            for i in range(ready_processes, len(input_list)):

                if input_list[i]["arrival_time"] <= current_time:
                    arrived_tasks.append(input_list[i])
                    ready_processes += 1

            arrived_tasks = sorted(arrived_tasks, key=lambda k: (k['burst_time'], k['arrival_time']))

            if arrived_tasks[0]['burst_time'] > 0:

                start_time.append(current_time)
                end_time.append(current_time + 1)

                output_list.append({"name": arrived_tasks[0]["name"],
                                    "start": start_time[-1],
                                    "end": end_time[-1]})

                arrived_tasks[0]['burst_time'] -= 1
                current_time += 1

                if arrived_tasks[0]['burst_time'] < 1:
                    arrived_tasks[0]['burst_time'] = 999999
                    done_processes += 1

                    # waiting_time.append(end_time[0] - input_list[0]["burst_time"] -
                    #                     input_list[0]["arrival_time"])
        return output_list

    else:
        start_time.append(0)
        end_time = [input_list[0]["burst_time"], ]

        for i in range(len(input_list)):
            if i == 0:
                output_list.append({"name": input_list[0]["name"], "start": start_time[0],
                                    "end": end_time[0]})
                waiting_time.append(start_time[0] - input_list[0]["arrival_time"])

            else:
                start_time.append(end_time[i - 1])
                end_time.append(input_list[i]["burst_time"] + end_time[i - 1])

                output_list.append({"name": input_list[i]["name"], "start": start_time[i],
                                    "end": end_time[i]})

                waiting_time.append(start_time[i] - input_list[i]["arrival_time"])

        return output_list, average(waiting_time)


# execute only if run as a script
if __name__ == "__main__":
    tasks = [{"name": "p1", "arrival_time": 0, "burst_time": 5},
             {"name": "p2", "arrival_time": 2, "burst_time": 1},
             {"name": "p3", "arrival_time": 4, "burst_time": 3}]

    print(sjf(tasks, False))
