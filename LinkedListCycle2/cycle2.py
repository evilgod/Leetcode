# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#// Hare and Tortoise algorithm:
# Tortoise walk 1 step
# Hare walk 2 steps 
# cycle start at x, meet at the node after m steps from x
# cycle length y, and k, t constants
# Tortoise total walk:x+ty+m 
# Hare total walk:x+ky+m
# Hare speed is twice of Tortoise, so the distance x+ky+m= 2(x+ty+m) ==> ky=2ty+x+m  (k-2t)y=x+m (x+m)mod y =0
# find m first, then Tortoise back to origin walk again, Hare keep walking from node m, x steps will meet Tortoise

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def detectCycle(self, head):
        
        if head is None or head.next is None: return null
        
        p = head.next
        q = head.next.next
        
        while q is not None and q.next is not None:
            if p!=q:
                p = p.next
                q = q.next.next
            else: 
                
                p = head
                while p!=q:
                    q = q.next
                    p = p.next            
                return p 
        return null