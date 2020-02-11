def minDepth(self, root: TreeNode) -> int:
    min_depth = 100000000000

    def getMinDepth(root: TreeNode, current_depth, min_depth):
        if root is not None:
            if root.left is None and root.right is None:
                if min_depth > current_depth: min_depth = current_depth
            min_depth = min(min_depth, getMinDepth(root.left, current_depth + 1, min_depth))
            min_depth = min(min_depth, getMinDepth(root.right, current_depth + 1, min_depth))
        return min_depth

    if root is None:
        return 0
    return getMinDepth(root, 1, min_depth)