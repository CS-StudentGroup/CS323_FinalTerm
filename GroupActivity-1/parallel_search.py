from multiprocessing import Process, Queue


def worker(sub_data, target, q, offset):
    for i in range(len(sub_data)):
        if target == sub_data[i]:
            q.put(i+offset)
            return
    q.put(-1)




def paralle_search(data, target):
    processes = []
    q = Queue()

    chunk_size = len(data) // 4

    for i in range(4):


