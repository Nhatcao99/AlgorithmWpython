def isUnivalTree(self, root: TreeNode) -> bool:
    def isUniUtil(root: TreeNode, value: int) -> bool:
        if root != None:
            if root.val != value: return False
            result = True
            result = isUniUtil(root.left, value) & isUniUtil(root.right, value)
            return result
        return True

    return isUniUtil(root, root.val)