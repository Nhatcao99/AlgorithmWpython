def nextLargerNodes(self, head: ListNode) -> List[int]:
    key = []
    val = []
    index = -1
    while head:
        key.append(head.val)
        val.append(0)
        index += 1
        i = index - 1
        while (i >= 0 and key[i] < key[index]):
            # should and upon meeting bigger element
            if (val[i] == 0):
                val[i] = key[index]
            i -= 1
        head = head.next
    return val