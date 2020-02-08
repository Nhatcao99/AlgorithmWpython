def sumNumbers(self, root: TreeNode) -> int:
    # use back tracking and DFF to get all the possi path into a matrix
    def DFSpath(root: TreeNode) -> List[int]:
        arr = []
        if root != None:
            if root.left is not None:
                arr1 = DFSpath(root.left)
                for c in arr1:
                    tmp = [root.val]
                    tmp.extend(c)
                    arr.append(tmp)
            if root.right is not None:
                arr1 = DFSpath(root.right)
                for c in arr1:
                    tmp = [root.val]
                    tmp.extend(c)
                    arr.append(tmp)
            if not arr:
                return [[root.val]]
        return arr

    matrix = DFSpath(root)
    sums = 0
    for c in matrix:
        index = len(c) - 1
        tmp = 0
        for i in c:
            sums += (i * (10 ** index))
            index -= 1
    return sums