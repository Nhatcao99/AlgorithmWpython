def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
    target_nodes = []
    dic_node_parent = {}

    def PostOrderTraversal(root: TreeNode):
        if root is not None:
            if root.left is not None:
                dic_node_parent[root.left] = root
                PostOrderTraversal(root.left)
            if root.right is not None:
                dic_node_parent[root.right] = root
                PostOrderTraversal(root.right)
            if root.val == target:
                target_nodes.append(root)

    # Post order so algo will delete the nodes from the end (leaves) first
    PostOrderTraversal(root)
    for c in target_nodes:
        if c.left is None and c.right is None:
            if c != root:
                tmp = dic_node_parent[c]
                if tmp.left == c:
                    tmp.left = None
                else:
                    tmp.right = None
            else:
                root = None
    return root