from multiprocessing import Process, Queue
import random

def data_creator(max_data_number, q):
    print('creating data!')
    for _ in range(max_data_number):
        data = random.random()
        q.put(data)
    q.put(None)

def data_consumer(q):
    while True:
        data = q.get()
        if data is None:
            break
        print('consumed data is{}'.format(data))

if __name__ == '__main__':
    q = Queue()
    max_data_number = 10
    process_creator = Process(target=data_creator, args=(max_data_number,q))
    process_consumer = Process(target=data_consumer, args=(q,))
    process_creator.start()
    process_consumer.start()

    q.close()
    q.join_thread()

    process_creator.join()
    process_creator.join()
