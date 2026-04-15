from multiprocessing import Process, Queue
from sequential_sort import merge_sort, merge

def sort_worker(sub_data, q):
    sorted_chunk = merge_sort(sub_data)
    q.put(sorted_chunk)

def parallel_sort(data, num_processes=4):
    if len(data) == 0:
        return []
        
    chunk_size = max(1, len(data) // num_processes)
    actual_processes = min(num_processes, len(data))
    
    chunks = []
    for i in range(actual_processes):
        start = i * chunk_size
        end = len(data) if i == actual_processes - 1 else (i + 1) * chunk_size
        chunks.append(data[start:end])

    q = Queue()
    processes = []

    for chunk in chunks:
        p = Process(target=sort_worker, args=(chunk, q))
        processes.append(p)
        p.start()

    sorted_chunks = []
    for _ in processes:
        sorted_chunks.append(q.get())

    for p in processes:
        p.join()

    if not sorted_chunks:
        return []

    result = sorted_chunks[0]
    for i in range(1, len(sorted_chunks)):
        result = merge(result, sorted_chunks[i])

    return result
