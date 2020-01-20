def DFS(root: TreeNode, height: int) -> int:
    if (root is None):
        return height
    height = height + 1
    return max(DFS(root.left, height), DFS(root.right, height))


return DFS(root, 0)