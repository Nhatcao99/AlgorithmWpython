def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    if root == p or root == q: return root

    def FindAllParent(root: 'TreeNode', store: dict, depth: int) -> dict:
        if root is None:
            return store
        if root.left is not None:
            store[root.left] = [root, depth + 1, root.left]
        if root.right is not None:
            store[root.right] = [root, depth + 1, root.right]
        store = FindAllParent(root.left, store, depth + 1)
        store = FindAllParent(root.right, store, depth + 1)
        return store

    dictionary = FindAllParent(root, {}, 0)
    node1, node2 = dictionary[p], dictionary[q]
    while (node1[0] != node2[0]):
        if node1[1] == node2[1]:
            node1 = dictionary[node1[0]]
            node2 = dictionary[node2[0]]
        elif node1[1] > node2[1]:
            if (node2[2] == node1[0]):
                return node1[0]
            node1 = dictionary[node1[0]]
        else:
            if (node1[2] == node2[0]):
                return node2[0]
            node2 = dictionary[node2[0]]
    return node1[0]
