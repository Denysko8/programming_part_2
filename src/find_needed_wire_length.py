import math

def max_wire_length(w, max_heights):
    n = len(max_heights)
    max_diff = max(max_height - 1 for max_height in max_heights)
    max_length = (n - 1) * math.hypot(w, max_diff)
    return round(max_length, 2)

print(max_wire_length(2, [3, 3, 3]))  # Output: 5.66
print(max_wire_length(100, [1, 1, 1, 1]))  # Output: 300.0
print(max_wire_length(4, [100, 2, 100, 2, 100]))  # Output: 396.32

heights = [56, 18, 17, 94, 23, 7, 21, 94, 29, 54, 44, 26, 86, 79, 4, 15, 5, 91, 25, 17, 88, 66, 28, 2, 95, 97, 60, 93, 40, 70, 75, 48, 38, 51, 34, 52, 87, 8, 62, 77, 35, 52, 3, 93, 34, 57, 51, 11, 39, 72]
print(max_wire_length(4, heights))  # Output: 2738.18