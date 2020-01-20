def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
    def inOrder(root: TreeNode, arr: List[int]) -> List[int]:
        if (root is None):
            arr.append(None)
            return arr
        arr.append(root.val)
        arr = inOrder(root.left, arr)
        arr = inOrder(root.right, arr)
        return arr

    p_arr = inOrder(p, [])
    q_arr = inOrder(q, [])
    leng1 = len(p_arr)
    leng2 = len(q_arr)
    if (leng1 != leng2): return False
    for i in range(0, leng1):
        if (p_arr[i] != q_arr[i]):
            return False
    return True