def calculate_work_duration(k, t, arr):

    work_duration = [0] * k

    if k < len(arr):
        board_per_painter = len(arr) // k
        remaining_boards = len(arr) % k
        start_index = 0
        for item in range(k):
            end_index = start_index + board_per_painter
            if remaining_boards > 0:
                end_index += 1
                remaining_boards -= 1

            work_duration[item] = sum(arr[start_index:end_index]) * t
            start_index = end_index
    else:
        for i in range(len(arr)):
            work_duration[i] = arr[i] * t

    result = max(work_duration)

    return result
