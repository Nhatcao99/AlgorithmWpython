def maxDepth(self, root: 'Node') -> int:
    def Depth(root: 'Node', depth: int):
        if root != None:
            depth += 1
            tmp = 0
            for c in root.children:
                tmp = max(tmp, Depth(c, depth))
            depth = max(tmp, depth)
        return depth

    return Depth(root, 0)