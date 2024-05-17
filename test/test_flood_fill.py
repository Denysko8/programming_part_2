import unittest
from src.flood_fill import flood_fill, read_input_file, write_output_file


class TestFloodFill(unittest.TestCase):
    def test_flood_fill(self):
        input_filename = 'materials/5-input.txt'
        with open(input_filename, 'w') as file:
            file.write('4, 4\n')
            file.write('2, 2\n')
            file.write('X\n')
            file.write('O, X, X, O\n')
            file.write('X, X, O, X\n')
            file.write('X, X, O, O\n')
            file.write('O, O, O, O\n')

        output_filename = 'materials/5-output.txt'

        height, width, start, new_color, matrix = read_input_file(input_filename)
        result_matrix = flood_fill(matrix, start, matrix[start[0]][start[1]], new_color)
        write_output_file(output_filename, result_matrix)

        expected_result = [
            ['O', 'X', 'X', 'O'],
            ['X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X']
        ]
        with open(output_filename, 'r') as file:
            actual_result = [list(map(str.strip, line.strip().split(', '))) for line in file]

        self.assertEqual(actual_result, expected_result)


if __name__ == '__main__':
    unittest.main()
