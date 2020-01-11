def getDecimalValue(self, head: ListNode) -> int:
    power = 0
    arr = []
    arr.append(head.val)
    while (head.next != None):
        head = head.next
        arr.append(head.val)
        power += 1
    sum = 0
    for i in range(0, len(arr)):
        if (arr[i] == 1):
            sum += 2 ** power
        power -= 1
    return sum
