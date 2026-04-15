import random
import time
from multiprocessing import Process, Queue

def generate_data(N):
    return [random.randint(1, 1000000) for _ in range(N)]

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

def worker(sub_data, q):
    sorted_chunk = merge_sort(sub_data)
    q.put(sorted_chunk)

def parallel_sort(data, num_processes=4):
    chunk_size = len(data) // num_processes
    chunks = [
        data[i:i + chunk_size]
        for i in range(0, len(data), chunk_size)
    ]

    q = Queue()
    processes = []

    for chunk in chunks:
        p = Process(target=worker, args=(chunk, q))
        processes.append(p)
        p.start()

    sorted_chunks = []
    for _ in processes:
        sorted_chunks.append(q.get())

    for p in processes:
        p.join()

    result = sorted_chunks[0]
    for i in range(1, len(sorted_chunks)):
        result = merge(result, sorted_chunks[i])

    return result

def test_dataset(size):
    print(f"\nTesting dataset size: {size}")

    data = generate_data(size)

    start = time.time()
    sorted_data = parallel_sort(data)
    end = time.time()

    print("Execution Time:", end - start, "seconds")
    print("Correctly sorted:", sorted_data == sorted(data))

if __name__ == "__main__":
    test_dataset(1000)
    test_dataset(100000)
    test_dataset(1000000)

    print("\nTesting already sorted data")
    sorted_case = list(range(100000))
    start = time.time()
    parallel_sort(sorted_case)
    end = time.time()
    print("Execution Time:", end - start, "seconds")
