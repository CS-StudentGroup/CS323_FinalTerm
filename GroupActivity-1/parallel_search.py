from multiprocessing import Process, Queue

def search_worker(sub_data, target, q, offset):
    for i in range(len(sub_data)):
        if target == sub_data[i]:
            q.put(i + offset)
            return
    q.put(-1)


def parallel_search(data, target, num_processes=4):
    if not data:
        return -1
        
    processes = []
    q = Queue()

    chunk_size = max(1, len(data) // num_processes)
    actual_processes = min(num_processes, len(data))

    for i in range(actual_processes):
        offset = chunk_size * i
        end_idx = len(data) if i == actual_processes - 1 else offset + chunk_size
        sub_data = data[offset:end_idx]
        
        p = Process(target=search_worker, args=(sub_data, target, q, offset))
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
