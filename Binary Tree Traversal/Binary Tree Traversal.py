# Pre-order traversal
def pre_order(node):
    if node is None:
        return []
    return_lst = [node.data]
    return_lst += pre_order(node.left)
    return_lst += pre_order(node.right)
    return return_lst

# In-order traversal
def in_order(node):
    if node is None:
        return []
    return_lst = in_order(node.left)
    return_lst += [node.data]
    return_lst += in_order(node.right)
    return return_lst

# Post-order traversal
def post_order(node):
    if node is None:
        return []
    return_lst = post_order(node.left)
    return_lst += post_order(node.right)
    return_lst += [node.data]
    return return_lst
