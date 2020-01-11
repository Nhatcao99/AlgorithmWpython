def middleNode(self, head: ListNode) -> ListNode:
    arr = []
    count = 0
    while head:
        arr.append(head)
        head = head.next
        count += 1

    return arr[int(count / 2)]