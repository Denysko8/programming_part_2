def check_forward(arr, k):
    final_list_forward = []
    mean = sum(arr) / len(arr)

    max_el = max(arr)
    if arr[-2] == max_el:
        max_el = max_el + arr[-1]
    elif arr[1] == max_el:
        max_el = max_el + arr[0]

    middle = (sum(arr) + (max_el + mean) / 2) / 2

    while middle >= max_el:

        lst_forward = []
        result = 0
        painters = k

        for i in range(len(arr)):
            if painters == 1:
                result += sum(arr[i:])
                lst_forward.append(result)
                break
            if result > middle:
                break
            result += arr[i]
            if result > middle or i == len(arr) - 1:
                if i == len(arr) - 1:
                    lst_forward.append(result)
                else:
                    lst_forward.append(result - arr[i])
                painters -= 1
                result = arr[i]

        final_list_forward.append(max(lst_forward))
        middle = int((middle + (max_el + mean) / 2) / 2)
    return final_list_forward


def check_backwards(arr, k):
    final_list_backward = []
    mean = sum(arr) / len(arr)

    max_el = max(arr)
    if arr[-2] == max_el:
        max_el = max_el + arr[-1]
    elif arr[1] == max_el:
        max_el = max_el + arr[0]

    middle = (sum(arr) + (max_el + mean) / 2) / 2

    while middle >= max_el:
        lst_backward = []
        result = 0
        painters = k

        for i in range(len(arr) - 1, -1, -1):
            if painters == 1:
                result += sum(arr[:i]) + arr[i]
                lst_backward.append(result)
                break
            result += arr[i]
            if result > middle or i == 0:
                if i == 0:
                    lst_backward.append(result)
                else:
                    lst_backward.append(result - arr[i])
                painters -= 1
                result = arr[i]

        final_list_backward.append(max(lst_backward))
        middle = int((middle + (max_el + mean) / 2) / 2)
    return final_list_backward


def final_result(painters, time, array):
    returned_list_forward = check_forward(array, painters)
    returned_list_backward = check_backwards(array, painters)
    gathered_list = returned_list_forward + returned_list_backward
    answer = min(gathered_list) * time
    return answer

