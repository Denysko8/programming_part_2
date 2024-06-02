import math


def calculate_distance_between_poles(width, height1, height2):
    return math.sqrt(width**2 + (height2 - height1) ** 2)


def max_wire_length_required(w, heights):
    num_poles = len(heights)
    if num_poles == 1:
        return 0
    top_length = 0
    bottom_length = 0
    if 0 < w <= 100:
        for i in range(num_poles - 1):
            if 0 < heights[i] <= 100:
                current_height = heights[i]
                next_height = heights[i + 1]
                max_to_max = calculate_distance_between_poles(w, current_height, next_height)
                min_to_min = calculate_distance_between_poles(w, 1, 1)
                min_to_max = calculate_distance_between_poles(w, 1, next_height)
                max_to_min = calculate_distance_between_poles(w, current_height, 1)
                next_top_length = max(
                    max_to_max + top_length, min_to_max + bottom_length
                )
                next_bottom_length = max(
                    max_to_min + top_length, min_to_min + bottom_length
                )
                top_length = next_top_length
                bottom_length = next_bottom_length
    return round(max(top_length, bottom_length), 2)
