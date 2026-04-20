def tree_by_levels(node):
    if node is None :
        return []
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
