def maxLevelSum(self, root: TreeNode) -> int:
    dic = {}  # depth and value

    def DFS(root: TreeNode, depth: int):
        if root is not None:
            if depth not in dic:
                dic[depth] = 0
            dic[depth] += root.val
            DFS(root.left, depth + 1)
            DFS(root.right, depth + 1)

    DFS(root, 1)
    depth, maximus = 1, dic[1]
    # print(dic)
    for key in dic:
        if dic[key] > maximus:
            # print(key , dic[key])
            maximus = dic[key]
            depth = key
    return depth