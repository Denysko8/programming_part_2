class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def is_tree_balanced(node: BinaryTree) -> bool:
    if node is None:
        return True

    left_height = height(node.left)
    right_height = height(node.right)

    if abs(left_height - right_height) > 1:
        return False

    return True


def height(node: BinaryTree) -> int:
    if node is None:
        return 0
    else:
        the_height = max(height(node.left), height(node.right)) + 1
        return the_height


root = BinaryTree(1)
root.left = BinaryTree(2)
root.left.left = BinaryTree(3)
root.left.left.left = BinaryTree(4)
root.left.left.left.left = BinaryTree(7)
root.right = BinaryTree(5)
root.right.right = BinaryTree(6)

print(is_tree_balanced(root))
