import unittest
from binary_tree_priority_queue import Node, PriorityQueue

class TestPriorityQueue(unittest.TestCase):
    def test_right_insertion(self):
        pq = PriorityQueue()
        pq.insert('Task 1', 3)
        pq.insert('Task 2', 1)
        pq.insert('Task 3', 2)
        pq.insert('Task 4', 4)

        expected_output = [('Task 2', 1), ('Task 3', 2), ('Task 1', 3), ('Task 4', 4)]
        self.assertEqual(pq._inorder_traversal(pq.root, []), expected_output)

    def test_empty_queue(self):
        pq = PriorityQueue()
        self.assertIsNone(pq.remove())

    def test_wrong_insertion(self):
        pq = PriorityQueue()
        pq.insert('Task 1', 3)
        pq.insert('Task 2', 1)
        pq.insert('Task 3', 4)
        pq.insert('Task 4', 2)

        expected_output = [('Task 1', 2), ('Task 4', 2), ('Task 1', 3), ('Task 3', 4)]
        self.assertNotEqual(pq._inorder_traversal(pq.root, []), expected_output)

if __name__ == '__main__':
    unittest.main()
