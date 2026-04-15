def sequential_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return i
    return -1