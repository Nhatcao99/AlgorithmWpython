def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
    def TakeSeq(root: TreeNode, arr: List[int]) -> List[int]:
        if (root is None):
            return arr
        if (root.left is None and root.right is None):
            arr.append(root.val)
            return arr
        arr = TakeSeq(root.left, arr)
        arr = TakeSeq(root.right, arr)
        return arr

    arr1, arr2 = TakeSeq(root1, []), TakeSeq(root2, [])
    leng1, leng2 = len(arr1), len(arr2)
    if (leng1 != leng2): return False
    for i in range(0, leng1):
        if arr1[i] != arr2[i]: return False
    return True
