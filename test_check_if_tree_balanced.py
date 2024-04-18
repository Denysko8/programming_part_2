import unittest

from main import BinaryTree, is_tree_balanced, height


class TestIsTreeBalanced(unittest.TestCase):
    def test_balanced_tree(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        root.left.left = BinaryTree(3)
        root.left.left.left = BinaryTree(4)
        root.right = BinaryTree(5)
        root.right.right = BinaryTree(6)
        self.assertTrue(is_tree_balanced(root))

    def test_unbalanced_tree(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        root.left.left = BinaryTree(3)
        root.left.left.left = BinaryTree(4)
        root.left.left.left.left = BinaryTree(8)
        root.right = BinaryTree(5)
        root.right.right = BinaryTree(6)
        self.assertFalse(is_tree_balanced(root))

    def test_empty_tree(self):
        self.assertTrue(is_tree_balanced(None))

    def test_single_node_tree(self):
        root = BinaryTree(1)
        self.assertTrue(is_tree_balanced(root))

    def test_two_node_tree(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        self.assertTrue(is_tree_balanced(root))


if __name__ == '__main__':
    unittest.main()
