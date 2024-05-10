def is_monotonic(arr):

    increasing = decreasing = True
    for i in range(0, len(arr) - 1):
        if arr[i] > arr[i + 1]:
            increasing = False
        if arr[i] < arr[i + 1]:
            decreasing = False

    return increasing or decreasing
