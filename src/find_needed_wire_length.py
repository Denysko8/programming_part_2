import math


def max_path_length(width, heights):
    heights_amount = len(heights)
    path_length = [[0] * (h + 1) for h in heights]

    for height in range(1, heights[0] + 1):
        path_length[0][height] = 0
    for i in range(1, heights_amount):
        for height_2 in range(1, heights[i] + 1):
            path_length[i][height_2] = max(
                path_length[i - 1][height1]
                + calculate_distance(width, height1, height_2)
                for height1 in range(1, heights[i - 1] + 1)
            )

    max_length = max(path_length[-1])

    return round(max_length, 2)


def calculate_distance(width, height1, height2):
    return math.sqrt(width**2 + (height2 - height1) ** 2)
