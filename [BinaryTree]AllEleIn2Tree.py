def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
    def inOrder(root: TreeNode, arr: List[int]) -> List[int]:
        if (root is None):
            return arr
        arr = inOrder(root.left, arr)
        arr.append(root.val)
        arr = inOrder(root.right, arr)
        return arr

    arr1 = inOrder(root1, [])
    arr2 = inOrder(root2, [])
    leng1, leng2 = len(arr1), len(arr2)
    i, j = 0, 0
    arr = []
    while (i < leng1 and j < leng2):
        if (arr1[i] <= arr2[j]):
            arr.append(arr1[i])
            i += 1
        else:
            arr.append(arr2[j])
            j += 1
    while (i < leng1):
        arr.append(arr1[i])
        i += 1
    while (j < leng2):
        arr.append(arr2[j])
        j += 1
    return arr