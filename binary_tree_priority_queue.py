class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
        self.left = None
        self.right = None

class PriorityQueue:
    def __init__(self):
        self.root = None

    def insert(self, value, priority):
        if not self.root:
            self.root = Node(value, priority)
        else:
            self._insert_recursively(self.root, value, priority)

    def _insert_recursively(self, node, value, priority):
        if priority <= node.priority:
            if node.left is None:
                node.left = Node(value, priority)
            else:
                self._insert_recursively(node.left, value, priority)
        else:
            if node.right is None:
                node.right = Node(value, priority)
            else:
                self._insert_recursively(node.right, value, priority)

    def _remove_min(self, node, parent):
        if node.left is None:
            if parent is None:
                self.root = node.right
            else:
                parent.left = node.right
            return node
        else:
            return self._remove_min(node.left, node)

    def remove(self):
        if not self.root:
            return None
        else:
            return self._remove_min(self.root, None)

    def _inorder_traversal(self, node, result):
        if node:
            self._inorder_traversal(node.left, result)
            result.append((node.value, node.priority))
            self._inorder_traversal(node.right, result)
        return result

    def display(self):
        result = []
        self._inorder_traversal(self.root, result)
        print("Priority Queue:", result)




