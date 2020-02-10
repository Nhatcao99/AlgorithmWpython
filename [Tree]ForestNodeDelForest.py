def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
    dic_value_node = {}  # use to effectively return the node
    dic_node_parent = {}  # use to effectively return the parent node
    dic_node_index = {root: 0}
    ls = [root]  # this is the result list

    # preparing data
    def DFS(root: TreeNode):
        if root is not None:
            if root.left is not None:
                dic_node_parent[root.left] = root
                DFS(root.left)
            dic_value_node[root.val] = root
            if root.right is not None:
                dic_node_parent[root.right] = root
                DFS(root.right)

    def ParentRejectChild(node: TreeNode):
        if node in dic_node_parent:
            parent = dic_node_parent[node]
            if node == parent.left: parent.left = None
            if node == parent.right: parent.right = None

    # solve the puzzle
    DFS(root)
    for c in to_delete:
        # add the children to the return list
        # delete connection from bbigger tree
        tmp = dic_value_node[c]
        ParentRejectChild(tmp)
        if tmp.left is not None:
            ls.append(tmp.left)
        if tmp.right is not None:
            ls.append(tmp.right)
        if tmp in ls:
            ls.remove(tmp)
    return ls