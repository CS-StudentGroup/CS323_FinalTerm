import time
from dataset import generate_random, generate_sorted, generate_reverse_sorted
from dataset import SMALL, MEDIUM, LARGE
from sequential_search import sequential_search
from sequential_sort import merge_sort
from parallel_search import parallel_search
from parallel_sort import parallel_sort

def measure_execution():
    datasets_to_test = {
        "Small (Random)": generate_random(SMALL),
        "Medium (Random)": generate_random(MEDIUM),
        "Large (Random)": generate_random(LARGE),
        "Medium (Sorted)": generate_sorted(MEDIUM),
        "Medium (Reverse)": generate_reverse_sorted(MEDIUM)
    }

    print("--- Performance Evaluation ---")
    print("Evaluating execution times for Sorting and Searching Algorithms.\n")
    
    for label, data in datasets_to_test.items():
        print(f"Evaluating: {label} [Size: {len(data):,}]")
        print("-" * 50)
        
        # 1. Sequential Sort
        start = time.time()
        seq_sorted = merge_sort(data)
        seq_sort_time = time.time() - start
        print(f"  Sequential Sort:   {seq_sort_time:.6f} seconds")
        
        # 2. Parallel Sort
        start = time.time()
        par_sorted = parallel_sort(data)
        par_sort_time = time.time() - start
        print(f"  Parallel Sort:     {par_sort_time:.6f} seconds")
        
        # Prepare for searching - target the last element of the dataset
        target = seq_sorted[-1]
        
        # 3. Sequential Search
        start = time.time()
        seq_idx = sequential_search(seq_sorted, target)
        seq_search_time = time.time() - start
        print(f"  Sequential Search: {seq_search_time:.6f} seconds (Found index: {seq_idx})")
        
        # 4. Parallel Search
        start = time.time()
        par_idx = parallel_search(seq_sorted, target)
        par_search_time = time.time() - start
        print(f"  Parallel Search:   {par_search_time:.6f} seconds (Found index: {par_idx})")
        
        print("\n")
        
if __name__ == "__main__":
    # Required wrap for multiple processes safely executing scripts on Windows
    measure_execution()
