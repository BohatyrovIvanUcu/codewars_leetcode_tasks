class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n

def assert_equals(actual, expected):
    assert actual == expected, f"Expected {expected}, got {actual}"
def tree_by_levels(node):
    queue  = [node]
    result = []
    while queue != []:
        item = queue.pop(0)
        result.append(item.value)
        if item.left is not None:
            queue.append(item.left)
        if item.right is not None:
            queue.append(item.right)
    return result


assert_equals(tree_by_levels(None), [])
assert_equals(tree_by_levels(Node(Node(None, Node(None, None, 4), 2), Node(Node(None, None, 5), Node(None, None, 6), 3), 1)), [1, 2, 3, 4, 5, 6])
