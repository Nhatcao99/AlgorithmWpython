def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
    def Sum(root: TreeNode, L: int, R: int, summing: int) -> int:
        if (root is None):
            return summing
        if (root.val >= L and root.val <= R):
            summing += root.val
        summing = Sum(root.left, L, R, summing)
        summing = Sum(root.right, L, R, summing)
        return summing

    return Sum(root, L, R, 0)