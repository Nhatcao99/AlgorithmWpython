def sumEvenGrandparent(self, root: TreeNode) -> int:
    # design a hashmap: key -> the node , value -> [the parent , bool depth(>= 2 -> have grand parent)]
    def getParent(root: TreeNode, h_map: dict, depth: int) -> dict:
        if root is not None:
            if root.left is not None:
                h_map[root.left] = [root, depth + 1]
            if root.right is not None:
                h_map[root.right] = [root, depth + 1]
            h_map = getParent(root.left, h_map, depth + 1)
            h_map = getParent(root.right, h_map, depth + 1)
        return h_map

    dic = getParent(root, {}, 0)
    sums = 0
    for key, val in dic.items():
        if val[1] >= 2:
            # with depth > 2 node have grand-parent
            if (dic[val[0]][0].val % 2 == 0):
                sums += key.val
    return sums