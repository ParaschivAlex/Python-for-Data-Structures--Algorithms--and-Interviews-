def trimBST(tree, minVal, maxVal):
    if not tree:
        return

    tree.left = trimBST(tree.left, minVal, maxVal)
    tree.right = trimBST(tree.right, minVal, maxVal)

    if minVal <= tree.val <= maxVal:
        return tree

    if tree.val < minVal:
        return tree.right

    if tree.val > maxVal:
        return tree.left


# def trim_bst(root, lower, upper):
#     if root is None:
#         return None
#     if root.val < lower:
#         return trim_bst(root.right, lower, upper)
#     if root.val > upper:
#         return trim_bst(root.left, lower, upper)
#     root.left = trim_bst(root.left, lower, upper)
#     root.right = trim_bst(root.right, lower, upper)
#     return root
