def postorderTraversal(self, root: TreeNode) -> List[int]:
    def DFSpost(root: TreeNode, arr: List[int]):
        if (root is None):
            return arr
        arr = DFSpost(root.left, arr)
        arr = DFSpost(root.right, arr)
        arr.append(root.val)
        return arr

    arr = DFSpost(root, [])
    return arr