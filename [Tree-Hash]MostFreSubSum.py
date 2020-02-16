def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
    dic, ls, value, highest, stack, leng = {}, [], 0, 0, [], 0  # get all the

    def getSumSub(root: TreeNode) -> int:
        if root != None:
            sums = root.val
            if root.left != None:
                sums += getSumSub(root.left)
                # getSumSub(root.left)
            if root.right != None:
                sums += getSumSub(root.right)
                # getSumSub(root.right)
            if sums not in dic:
                dic[sums] = 1
            else:
                dic[sums] += 1
            return sums
        return 0

    getSumSub(root)
    for key, val in dic.items():
        if val > highest:
            value, highest = key, val
            while leng > 0:
                stack.pop()
                leng -= 1
        if val == highest:
            leng += 1
            stack.append(key)
    return stack