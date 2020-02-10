def deepestLeavesSum(self, root: TreeNode) -> int:
    dic = {}  # too story the ele and their depth

    def DFSsums(root: TreeNode, depth: int):
        if root is not None:
            if root.val not in dic:
                dic[root.val] = [depth]
            else:
                dic[root.val].append(depth)
            depth = max(DFSsums(root.left, depth + 1), DFSsums(root.right, depth + 1))
        return depth

    deepest = DFSsums(root, 0)
    result = 0
    for key, val in dic.items():
        for c in val:
            if c == deepest - 1:
                result += key
    return result