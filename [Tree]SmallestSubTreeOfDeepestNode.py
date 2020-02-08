def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
    dic = {}  # store the node's parent and depth

    def getParentDepth(root: TreeNode, depth: int) -> int:
        deep = depth
        if root != None:
            if root.left != None:
                dic[root.left] = [root, depth + 1]
                deep = max(deep, getParentDepth(root.left, depth + 1))
            if root.right != None:
                dic[root.right] = [root, depth + 1]
                deep = max(deep, getParentDepth(root.right, depth + 1))
        return deep

    max_d = getParentDepth(root, 0)
    chosen = []
    for key, val in dic.items():
        # get the key with the depth
        if val[1] == max_d:
            chosen.append(key)
        # track to the lowest common ancestor
    leng = len(chosen)
    if leng == 0: return root

    def findCommonAncestor(root1: TreeNode, root2: TreeNode) -> TreeNode:
        while (root1 != root2):
            if (dic[root1][1] > dic[root2][1]):
                root1 = dic[root1][0]
            elif (dic[root1][1] < dic[root2][1]):
                root2 = dic[root2][0]
            else:
                root1, root2 = dic[root1][0], dic[root2][0]
        return root1

    while (leng > 1):
        tmp1, tmp2 = chosen.pop(0), chosen.pop(0)
        chosen.append(findCommonAncestor(tmp1, tmp2))
        leng -= 1
    return chosen[0]