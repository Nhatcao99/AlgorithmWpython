def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    st1, st2 = [], []
    while l1 != None:
        st1.append(l1.val)
        l1 = l1.next
    while l2 != None:
        st2.append(l2.val)
        l2 = l2.next
    leng1, leng2 = len(st1), len(st2)
    while leng1 < leng2:
        st1.insert(0, 0)
        leng1 += 1
    while leng2 < leng1:
        st2.insert(0, 0)
        leng2 += 1
    remember_1, index = 0, leng1 - 1
    while (index >= 0):
        st1[index] += st2[index] + remember_1
        if st1[index] >= 10:
            st1[index] = st1[index] % 10
            remember_1 = 1
        else:
            remember_1 = 0
        index -= 1
    if (remember_1 == 1):
        st1.insert(0, 1)
        leng1 += 1
    root = ListNode(0)
    tmp = root
    for i in range(0, leng1):
        cur = ListNode(st1[i])
        tmp.next = cur
        tmp = tmp.next
    return root.next