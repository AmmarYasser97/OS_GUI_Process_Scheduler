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
    current_time = 0

    input_list.sort(key=lambda k: (k['arrival_time'], k['burst_time']))
    start_time = [input_list[0]['arrival_time']]

    if is_preemptive:
        end_time = []
        arrived_tasks = []
        last_worked_process = input_list[0]['task']
        done_processes = 0
        ready_processes = 0
        idle_time = 0

        while done_processes < len(input_list):
            for i in range(ready_processes, len(input_list)):
                if input_list[i]['arrival_time'] <= current_time:
                    arrived_tasks.append(input_list[i].copy())
                    ready_processes += 1

            arrived_tasks.sort(key=lambda k: (k['burst_time'], k['arrival_time']))

            if len(arrived_tasks) > done_processes:
                if arrived_tasks[0]['burst_time'] > 0:
                    if last_worked_process == arrived_tasks[0]['task']:
                        pass
                    else:
                        # Push the working process in the output_list if it just has been interrupted
                        end_time.append(current_time - idle_time)
                        idle_time = 0
                        output_list.append({"Task": last_worked_process,
                                            "Start": start_time[-1],
                                            "Finish": end_time[-1]})

                        # Start execute the next ready process
                        start_time.append(current_time)
                        last_worked_process = arrived_tasks[0]['task']

                    arrived_tasks[0]['burst_time'] -= 1
                    current_time += 1

                    # Check if the process has finished put it in the last of the Queue
                    if arrived_tasks[0]['burst_time'] < 1:
                        arrived_tasks[0]['burst_time'] = 999999

                        done_processes += 1

                    # Append the last executed process before exit from the while loop
                    if done_processes == len(input_list):
                        if len(input_list) == 1:
                            end_time.append(current_time)
                            output_list.append({"Task": last_worked_process,
                                                "Start": start_time[-1],
                                                "Finish": end_time[-1]})
                        else:
                            end_time.append(current_time)
                            output_list.append({"Task": last_worked_process,
                                                "Start": start_time[-1],
                                                "Finish": end_time[-1]})
            else:
                current_time += 1
                idle_time += 1
        # Calculate the waiting time for every process
        temp_list = []
        for j in reversed(range(len(output_list))):
            current_process = next(item for item in input_list
                                   if item["task"] == output_list[j]["Task"])
            if current_process not in temp_list:
                waiting_time.append(end_time[j] -
                                    current_process['arrival_time'] -
                                    current_process['burst_time'])
                temp_list.append(current_process)

        return output_list, average(waiting_time)
    else:
        end_time = [input_list[0]['burst_time'] + start_time[0], ]

        for i in range(len(input_list)):
            if i == 0:
                output_list.append({"Task": input_list[0]['task'], "Start": start_time[0],
                                    "Finish": end_time[0]})
                waiting_time.append(start_time[0] - input_list[0]['arrival_time'])
                current_time = end_time[0]

            else:
                while input_list[i]["arrival_time"] > current_time or end_time[i - 1] > current_time:
                    current_time += 1
                start_time.append(current_time)
                end_time.append(input_list[i]['burst_time'] + current_time)

                output_list.append({"Task": input_list[i]['task'], "Start": start_time[i],
                                    "Finish": end_time[i]})

                waiting_time.append(start_time[i] - input_list[i]['arrival_time'])
        if waiting_time<0:
            waiting_time=0
        return output_list, average(waiting_time)


# execute only if run as a script
if __name__ == "__main__":
    tasks = [{"task": "p1", "arrival_time": 0, "burst_time": 6},
             {"task": "p2", "arrival_time": 4, "burst_time": 1},
             {"task": "p3", "arrival_time": 8, "burst_time": 1}]

    print(sjf(tasks, True))
