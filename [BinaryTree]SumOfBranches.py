def deepestLeavesSum(self, root: TreeNode) -> int:
    def DFSsum(root: TreeNode, suma: int) -> int:
        if (root is None):
            return suma
        suma += root.val
        x = max(DFSsum(root.left, 0), DFSsum(root.right, 0))
        return suma + x

    suma = DFSsum(root, 0)
    return suma