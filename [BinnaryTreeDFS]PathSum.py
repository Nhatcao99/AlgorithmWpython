def hasPathSum(self, root: TreeNode, sum: int) -> bool:
    def DFSsum(root: TreeNode, suma: int, dic: List[int]) -> List[int]:
        if (root is None):
            # return upon reaching none
            return dic
        if (root.left is None and root.right is None):
            # reach the left so this is counted as a path
            suma += root.val
            dic.append(suma)
            return dic
        suma += root.val
        # store path sum in dictionary
        dic = DFSsum(root.left, suma, dic)
        dic = DFSsum(root.right, suma, dic)
        return dic

    dic = DFSsum(root, 0, [])
    print(dic)
    return sum in dic