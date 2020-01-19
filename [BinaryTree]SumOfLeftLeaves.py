def sumOfLeftLeaves(self, root: TreeNode) -> int:
    def DFSleft(root: TreeNode, sum_left, isLeft) -> int:
        if (root is None):
            return sum_left
        if (isLeft and root.left is None and root.right is None):
            sum_left += root.val
        tmp_left = DFSleft(root.left, 0, True)
        tmp_right = DFSleft(root.right, 0, False)
        return sum_left + tmp_left + tmp_right

    suma = DFSleft(root, 0, False)
    return suma