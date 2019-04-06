def average(lst):
    return sum(lst) / len(lst)


def sjf(input_list, is_preemptive=False):
    """
    Function implementing the Short Job First (SJF) algorithm CPU scheduler

    :param input_list: a list of CPU process which needed to be scheduled
    :param is_preemptive: scheduling is preemptive or non-preemptive
    :return: the scheduled list of processes and the avg. waiting time
    """
    output_list = []
    waiting_time = []
    start_time = [0]
    input_list.sort(key=lambda k: (k['arrival_time'], k['burst_time']))

    if is_preemptive:
        end_time = []
        arrived_tasks = []
        last_worked_process = input_list[0]['name']
        current_time = 0
        done_processes = 0
        ready_processes = 0

        while done_processes < len(input_list):
            for i in range(ready_processes, len(input_list)):
                if input_list[i]['arrival_time'] <= current_time:
                    arrived_tasks.append(input_list[i].copy())
                    ready_processes += 1

            arrived_tasks.sort(key=lambda k: (k['burst_time'], k['arrival_time']))

            if arrived_tasks[0]['burst_time'] > 0:
                if last_worked_process == arrived_tasks[0]['name']:
                    pass
                else:
                    # Push the working process in the output_list if it just has been interrupted
                    end_time.append(current_time)
                    output_list.append({"name": last_worked_process,
                                        "start": start_time[done_processes],
                                        "end": end_time[done_processes]})

                    # Start execute the next ready process
                    start_time.append(current_time)
                    last_worked_process = arrived_tasks[0]['name']

                arrived_tasks[0]['burst_time'] -= 1
                current_time += 1

                # Check if the process has finished put it in the last of the Queue
                if arrived_tasks[0]['burst_time'] < 1:
                    arrived_tasks[0]['burst_time'] = 999999
                    done_processes += 1

                    # Append the last executed process before exit from the while loop
                    if done_processes == len(input_list):
                        end_time.append(current_time)
                        output_list.append({"name": last_worked_process,
                                            "start": start_time[done_processes],
                                            "end": end_time[done_processes]})

        # Calculate the waiting time for every process
        temp_list = []
        for j in reversed(range(len(output_list))):
            current_process = next(item for item in input_list
                                   if item["name"] == output_list[j]["name"])
            if current_process not in temp_list:
                waiting_time.append(end_time[j] -
                                    current_process['arrival_time'] -
                                    current_process['burst_time'])
                temp_list.append(current_process)

        return output_list, average(waiting_time)
    else:
        end_time = [input_list[0]['burst_time'], ]

        for i in range(len(input_list)):
            if i == 0:
                output_list.append({"name": input_list[0]['name'], "start": start_time[0],
                                    "end": end_time[0]})
                waiting_time.append(start_time[0] - input_list[0]['arrival_time'])

            else:
                start_time.append(end_time[i - 1])
                end_time.append(input_list[i]['burst_time'] + end_time[i - 1])

                output_list.append({"name": input_list[i]['name'], "start": start_time[i],
                                    "end": end_time[i]})

                waiting_time.append(start_time[i] - input_list[i]['arrival_time'])

        return output_list, average(waiting_time)


# execute only if run as a script
if __name__ == "__main__":
    tasks = [{"name": "p1", "arrival_time": 0, "burst_time": 5},
             {"name": "p2", "arrival_time": 2, "burst_time": 1},
             {"name": "p3", "arrival_time": 4, "burst_time": 3}]

    print(sjf(tasks, True))
