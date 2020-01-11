def oddEvenList(self, head: ListNode) -> ListNode:
    odds = ListNode(0)
    evens = ListNode(0)
    index = 1
    oddsHead = head
    evensHead = evens
    while head:  # using while head to avoid NoneType error
        if (index % 2 != 0):
            odds.next = head
            odds = odds.next
            # use next in stead of val to advoid NoneType error
        else:
            evens.next = head
            evens = evens.next
        head = head.next
        index += 1
    evens.next = None
    odds.next = evensHead.next
    return oddsHead  # zero at start