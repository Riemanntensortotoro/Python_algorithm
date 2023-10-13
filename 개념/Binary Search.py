def BS(arr, value):
    start, end = 0, len(arr) - 1
    
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] < value:
            start = mid + 1
        else:
            end = mid - 1

    return start