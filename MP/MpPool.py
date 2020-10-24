from multiprocessing import Pool
import time
import os

def my_func(work):
    print("일(={0})에 Process ID = {1}".format(work, os.getpid()))
    time.sleep(1)
    return work

if __name__ == '__main__':
    p = Pool(3)
    startTime = int(time.time())
    print(p.map(my_func, range(0, 30)))
    endTime = int(time.time())
    print("작업 시간 = 약{0}s", (endTime - startTime))