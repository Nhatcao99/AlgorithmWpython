def deleteDuplicates(self, head: ListNode) -> ListNode:
    tmp = head
    hash_tab = {}
    while tmp != None:
        if tmp.val not in hash_tab:
            hash_tab[tmp.val] = 0
        hash_tab[tmp.val] += 1
        tmp = tmp.next
    new = ListNode(0)
    new_head = new
    for key, val in hash_tab.items():
        if val == 1:
            new.next = ListNode(key)
            new = new.next
    return new_head.next