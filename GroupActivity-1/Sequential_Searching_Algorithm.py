import random
import time

SMALL = 1_000
MEDIUM = 100_000
LARGE = 1_000_000

def generate_random(n):
    return [random.randint(1, 1000000) for _ in range(n)]

def generate_sorted(n):
    return list(range(1, n + 1))

def generate_reverse_sorted(n):
    return list(range(n, 0, -1))

def sequential_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return i
    return -1

def test_search(data, target, label):
    start = time.time()
    
    result = sequential_search(data, target)
    
    end = time.time()

    print(f"{label}:")
    if result != -1:
        print(f"Found at index {result}")
    else:
        print("Not found")
    print(f"Time taken: {end - start:.6f} seconds\n")

if __name__ == "__main__":
    
    small_data = generate_random(SMALL)
    test_search(small_data, small_data[-1], "Small Dataset (Random)")

    medium_data = generate_random(MEDIUM)
    test_search(medium_data, medium_data[-1], "Medium Dataset (Random)")

    large_data = generate_random(LARGE)
    test_search(large_data, large_data[-1], "Large Dataset (Random)")

    sorted_data = generate_sorted(MEDIUM)
    test_search(sorted_data, sorted_data[-1], "Sorted Dataset")

    reverse_data = generate_reverse_sorted(MEDIUM)
    test_search(reverse_data, reverse_data[-1], "Reverse Sorted Dataset")
    
    