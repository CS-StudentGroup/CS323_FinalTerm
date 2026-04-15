from dataset import generate_random, generate_sorted, generate_reverse_sorted, SMALL, MEDIUM

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    left = merge_sort(left)
    right = merge_sort(right)
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

if __name__ == "__main__":
    print("\n1. Random array (small):")
    test_random = generate_random(10)
    print(f"   Original:  {test_random}")
    sorted_random = merge_sort(test_random)
    print(f"   Sorted:    {sorted_random}")
    
    print("\n2. Already sorted array:")
    test_sorted = generate_sorted(10)
    print(f"   Original:  {test_sorted}")
    sorted_array = merge_sort(test_sorted)
    print(f"   Sorted:    {sorted_array}")
    
    print("\n3. Reverse sorted array:")
    test_reverse = generate_reverse_sorted(10)
    print(f"   Original:  {test_reverse}")
    sorted_reverse = merge_sort(test_reverse)
    print(f"   Sorted:    {sorted_reverse}")
    
    print("\n4. Larger arrays:")
    for size_name, size in [("SMALL", SMALL), ("MEDIUM", MEDIUM)]:
        data = generate_random(size)
        result = merge_sort(data)
        print(f"   {size_name} ({size:,} elements): Sorted successfully")