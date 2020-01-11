def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    merge = ListNode(0)
    result = merge
    while l1:
        if l2:
            if (l1.val < l2.val):
                merge.next = l1
                l1 = l1.next
            else:
                merge.next = l2
                l2 = l2.next
        else:
            merge.next = l1
            l1 = l1.next
        merge = merge.next
    while l2:  # incase l2 is longer than l1
        merge.next = l2
        merge = merge.next
        l2 = l2.next
    return result.next  # first ele equi 0