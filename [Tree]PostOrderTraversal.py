def postorder(self, root: 'Node') -> List[int]:
    def postTraversal(root: TreeNode, arr: List[int]) -> List[int]:
        if root is not None:
            for c in root.children:
                arr = postTraversal(c, arr)
            arr.append(root.val)
            return arr

    arr = postTraversal(root, [])
    return arr