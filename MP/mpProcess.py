import os
import time
from multiprocessing import Process


def seconds_timer(end_time):
    start_time = time.time()
    while True:
        time.sleep(0.001)
        if time.time() - start_time >= end_time:
            break
    proc = os.getpid()
    print('{0} seconds have elapsed by process id: {1}'.format(end_time, proc))


if __name__ == '__main__':
    end_time_list = [5, 5, 5]
    procs = []

    startTime = int(time.time())
    for end_time in end_time_list:
        proc = Process(target=seconds_timer, args=(end_time,))
        procs.append(proc)
        proc.start()

    for proc in procs:
        proc.join()
    endTime = int(time.time())
    print("작업 시간 = 약 {0}s".format(endTime - startTime))
