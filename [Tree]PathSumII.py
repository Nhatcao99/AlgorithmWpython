def pathSum(self, root: TreeNode, sums: int) -> List[List[int]]:
    ls = []

    def path(root: TreeNode, sums: int, arr: List[int], target: int):
        if root is not None:
            sums += root.val
            arr1 = []
            arr1.extend(arr)
            arr1.append(root.val)
            if sums == target and root.left == None and root.right == None:
                ls.append(arr1)
            path(root.left, sums, arr1, target)
            path(root.right, sums, arr1, target)

    path(root, 0, [], sums)
    return ls