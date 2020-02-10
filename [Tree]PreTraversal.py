def preorder(self, root: 'Node') -> List[int]:
    def preTraversal(root: TreeNode, arr: List[int]) -> List[int]:
        if root is not None:
            arr.append(root.val)
            for c in root.children:
                arr = preTraversal(c, arr)
            return arr

    arr = preTraversal(root, [])
    return arr