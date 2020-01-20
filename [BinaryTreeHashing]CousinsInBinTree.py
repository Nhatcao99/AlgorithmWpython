def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
    dic = {}
    dic[root.val] = [0, 0]

    def getNodeAndHeight(root: TreeNode, height: int):
        if (root is None):
            return
        if (root.left is not None):
            dic[root.left.val] = [root.val, height + 1]
        if (root.right is not None):
            dic[root.right.val] = [root.val, height + 1]
        getNodeAndHeight(root.left, height + 1)
        getNodeAndHeight(root.right, height + 1)

    getNodeAndHeight(root, 0)
    s1, s2 = dic[x], dic[y]
    return (s1[0] != s2[0] and s1[1] == s2[1])
