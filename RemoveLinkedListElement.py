def removeElements(self, head: ListNode, val: int) -> ListNode:
    result = ListNode(0)
    result.next = head
    prev = result
    # the problem isn't as hard as I thougt
    # there will be no consecutive delete element in the test cases
    # use simple iteration
    while head:
        if head.val == val:
            prev.next = head.next
        else:
            prev = head
        head = head.next
    return result.next