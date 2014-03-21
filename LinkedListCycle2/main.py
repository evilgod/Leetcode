import cycle2

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

a = ListNode(2)
b = ListNode(4)
c = ListNode(9)
d = ListNode(4)

a.next = b
b.next = c
c.next = d
d.next = b

result = cycle2.Solution()
#print result.detectCycle(a).val
print result.detectCycle(a)