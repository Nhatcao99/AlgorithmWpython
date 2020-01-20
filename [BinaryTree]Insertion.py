def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
    tmp = root
    while (root is not None):
        prev = root
        isLeft = True
        if (root.val < val):
            root = root.right
            isLeft = False
        else:
            root = root.left
            isLeft = True
        if (root is None):
            root = TreeNode(val)
            if (isLeft):
                prev.left = root
            else:
                prev.right = root
            break
    return tmp