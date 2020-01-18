def inOrder(root:TreeNode , ls) -> List[int]:
    if(root is None):
        return ls
    ls = inOrder(root.left,ls)
    ls.append(root.val)
    ls = inOrder(root.right,ls)
    return ls
def kthSmallest(self, root: TreeNode, k: int) -> int:
    ls = inOrder(root, [])
    return ls[k - 1]
    inOrder(root)
    return ls[k - 1]