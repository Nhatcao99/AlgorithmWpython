def smallestFromLeaf(self, root: TreeNode) -> str:
    min_string = "z" * 8501

    def compare_string_min(s1: str, s2: str) -> str:
        if s1 < s2: return s1
        return s2

    def getAllString(root: TreeNode, string: str, min_string: str):
        # if root is node add to the strings
        string = "".join((chr(root.val + 97), string))
        if root.left is None and root.right is None:
            if min_string > string: min_string = string
        if root.left is not None:
            min_string = compare_string_min(min_string, getAllString(root.left, string, min_string))
        if root.right is not None:
            min_string = compare_string_min(min_string, getAllString(root.right, string, min_string))
        return min_string

    return getAllString(root, "", min_string)
