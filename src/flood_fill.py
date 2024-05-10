from typing import List, Tuple
from collections import deque


def flood_fill(matrix: List[List[str]], start: Tuple[int, int], target_color: str, new_color: str) -> List[List[str]]:
    queue = deque([start])
    visited = set()
    while queue:
        x, y = queue.popleft()
        if (x, y) in visited or x < 0 or y < 0 or x >= len(matrix) or y >= len(matrix[0]):
            continue
        if matrix[x][y] == target_color:
            matrix[x][y] = new_color
            visited.add((x, y))
            queue.extend([(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)])
    return matrix


def read_input_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        height, width = map(int, file.readline().strip().split(','))
        start = tuple(map(int, file.readline().strip().split(',')))
        new_color = file.readline().strip()
        matrix = [list(map(str.strip, file.readline().strip().split(', '))) for _ in range(height)]
    return height, width, start, new_color, matrix


def write_output_file(filename, matrix):
    with open(filename, 'w', encoding='utf-8') as file:
        for row in matrix:
            file.write(', '.join(row) + '\n')


def main():

    input_filename = '../materials/5-input.txt'
    output_filename = '../materials/5-output.txt'


    height, width, start, new_color, matrix = read_input_file(input_filename)
    result_matrix = flood_fill(matrix, start, matrix[start[0]][start[1]], new_color)
    write_output_file(output_filename, result_matrix)


if __name__ == "__main__":
    main()