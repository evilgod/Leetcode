import merList

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
a = ListNode(1)
b = ListNode(2)
c = ListNode(4)
d = ListNode(5)
e = ListNode(8)
        
a.next = b
b.next = c
#d.next = e
    
result= merList.Solution().mergelist(d, a)
while result is not None:
    print result.val
    result=result.next