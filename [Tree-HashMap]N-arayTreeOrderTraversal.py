def levelOrder(self, root: 'Node') -> List[List[int]]:
    dic, ls = {}, []

    def PreOrderWDepth(root: Node, depth: int):
        if root is not None:
            if depth not in dic:
                dic[depth] = []
            dic[depth].append(root.val)
            for c in root.children:
                PreOrderWDepth(c, depth + 1)

    PreOrderWDepth(root, 0)
    for key, val in dic.items():
        ls.append(val)
    return ls