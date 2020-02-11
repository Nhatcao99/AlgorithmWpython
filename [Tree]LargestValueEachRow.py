def largestValues(self, root: TreeNode) -> List[int]:
    dic_depth_node = {}

    def getValueByDepth(root: TreeNode, depth: int):
        if root is not None:
            if depth not in dic_depth_node:
                dic_depth_node[depth] = root.val
            if dic_depth_node[depth] < root.val:
                dic_depth_node[depth] = root.val
            getValueByDepth(root.left, depth + 1)
            getValueByDepth(root.right, depth + 1)

    getValueByDepth(root, 0)
    ls = []
    for key, value in dic_depth_node.items():
        ls.append(value)
    return ls