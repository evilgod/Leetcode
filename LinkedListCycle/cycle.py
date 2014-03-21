# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        
        if head is None or head.next is None: return False
        
        p = head.next
        q = head.next.next
        
        while q is not None and q.next is not None:
            if p!=q:
                p = p.next
                q = q.next.next
            else: 
                return True
        return False