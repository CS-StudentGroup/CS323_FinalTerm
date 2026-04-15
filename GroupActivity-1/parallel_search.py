from multiprocessing import Process, Queue

def worker(sub_data, target, q, offset):
    for i in range(len(sub_data)):
        if target == sub_data[i]:
            q.put(i+offset)
            return
    q.put(-1)


def parallel_search(data, target):
    processes = []
    q = Queue()

    chunk_size = len(data) // 4

    for i in range(4):
        offset = chunk_size * i
        sub_data = data[offset:offset+chunk_size]
        p = Process(target=worker, args=(sub_data, target, q, offset))
        processes.append(p)
        p.start()

    result = -1
    for _ in processes:
        res = q.get()
        if res != -1:
            result = res

    for p in processes:
        p.join()

    return result

