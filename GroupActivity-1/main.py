import sys
import os
import time
import datetime
from dataset import generate_random, generate_sorted, generate_reverse_sorted, SMALL, MEDIUM, LARGE
from sequential_search import sequential_search
from sequential_sort import merge_sort
from parallel_search import parallel_search
from parallel_sort import parallel_sort

def test_dataset(data, size_label, dist_label, print_data=False):
    label = f"{size_label} {dist_label} Dataset"
    output_lines = []
    
    def log_print(msg=""):
        print(msg)
        output_lines.append(msg)

    log_print(f"\n--- Testing: {label} (Size: {len(data):,}) ---")
    if print_data and len(data) <= 50:
        log_print(f"Original Data:\n{data}")
    elif print_data:
        log_print(f"Original Data: {data[:10]} ... {data[-10:]}")
        
    log_print("\n[ Performance Evaluation - SORTING ]")
    
    start_time = time.time()
    seq_sorted = merge_sort(data)
    seq_sort_time = time.time() - start_time
    log_print(f"  Sequential Sort: {seq_sort_time:.6f} seconds")
    
    start_time = time.time()
    par_sorted = parallel_sort(data)
    par_sort_time = time.time() - start_time
    log_print(f"  Parallel Sort:   {par_sort_time:.6f} seconds")
    
    if seq_sorted == par_sorted == sorted(data):
        log_print("  -> RESULT: Sorting functions correctly matched sorted algorithm.")
    else:
        log_print("  -> ERROR: Sorting algorithms produced incorrect outputs!")
        
    if print_data and len(data) <= 50:
        log_print(f"\nSorted Result:\n{seq_sorted}")
        
    target = seq_sorted[-1]
    log_print(f"\n[ Performance Evaluation - SEARCHING ]")
    log_print(f"Searching for target element: {target} (Worst-case scenario at end of array)")
    
    start_time = time.time()
    seq_idx = sequential_search(seq_sorted, target)
    seq_search_time = time.time() - start_time
    log_print(f"  Sequential Search: {seq_search_time:.6f} seconds (Found index: {seq_idx})")
    
    start_time = time.time()
    par_idx = parallel_search(seq_sorted, target)
    par_search_time = time.time() - start_time
    log_print(f"  Parallel Search:   {par_search_time:.6f} seconds (Found index: {par_idx})")
    
    if seq_idx != -1 and par_idx != -1 and seq_sorted[seq_idx] == target and seq_sorted[par_idx] == target:
        log_print("  -> RESULT: Search finding algorithms successfully queried valid matching indexes!")
    else:
        log_print("  -> ERROR: Search algorithms produced incorrect index!")

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    docs_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "docs")
    os.makedirs(docs_dir, exist_ok=True)
    
    safe_dist_label = dist_label.replace(" ", "-")
    filename = f"{size_label}-{safe_dist_label}-{timestamp}.txt"
    filepath = os.path.join(docs_dir, filename)
    
    try:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write("\n".join(output_lines) + "\n")
        print(f"\n-> Testing complete. Results saved explicitly into folder path: GroupActivity-1/docs/{filename}")
    except Exception as e:
        print(f"\n-> Warning: Failed to write benchmark logs ({e})")

    dataset_dir = os.path.join(docs_dir, "datasetGeneration")
    os.makedirs(dataset_dir, exist_ok=True)
    dataset_filepath = os.path.join(dataset_dir, filename)
    
    try:
        with open(dataset_filepath, "w", encoding="utf-8") as f:
            f.write(str(data))
        print(f"-> Actual Dataset array strictly saved into folder path: GroupActivity-1/docs/datasetGeneration/{filename}")
    except Exception as e:
        print(f"-> Warning: Failed to write actual dataset ({e})")


def main_menu():
    while True:
        print("\n" + "="*45)
        print("  CS323 Parallel vs Sequential Algorithms Menu")
        print("="*45)
        print(f"1. Test Small Dataset ({SMALL:,} items)")
        print(f"2. Test Medium Dataset ({MEDIUM:,} items)")
        print(f"3. Test Large Dataset ({LARGE:,} items) !! Might take some time !!")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == '4':
            print("Exiting program... Goodbye!")
            sys.exit(0)
            
        if choice not in ['1', '2', '3']:
            print("Invalid choice. Please select from 1-4.")
            continue
            
        size = 0
        size_label = ""
        
        if choice == '1':
            size = SMALL
            size_label = "Small"
        elif choice == '2':
            size = MEDIUM
            size_label = "Medium"
        elif choice == '3':
            size = LARGE
            size_label = "Large"

        print(f"\nSelect Data Distribution for {size_label} dataset:")
        print("1. Random")
        print("2. Sorted")
        print("3. Reverse Sorted")
        
        dist_choice = input("Enter choice (1-3): ").strip()
        
        if dist_choice == '1':
            print(f"\nGenerating {size_label} Random dataset... please wait.")
            data = generate_random(size)
            test_dataset(data, size_label, "Random", print_data=(size <= 50))
        elif dist_choice == '2':
            print(f"\nGenerating {size_label} Sorted dataset... please wait.")
            data = generate_sorted(size)
            test_dataset(data, size_label, "Sorted", print_data=(size <= 50))
        elif dist_choice == '3':
            print(f"\nGenerating {size_label} Reverse Sorted dataset... please wait.")
            data = generate_reverse_sorted(size)
            test_dataset(data, size_label, "Reverse Sorted", print_data=(size <= 50))
        else:
            print("Invalid distribution choice. Returning to main menu.")

if __name__ == '__main__':
    main_menu()
