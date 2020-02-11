def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
    def insert(root, node: TreeNode) -> TreeNode:
        if root is None:
            root = node
        else:
            if root.val > node.val:
                root.left = insert(root.left, node)
            else:
                root.right = insert(root.right, node)
        return root

    root = None
    for i in preorder:
        new_node = TreeNode(i)
        root = insert(root, new_node)
    return root