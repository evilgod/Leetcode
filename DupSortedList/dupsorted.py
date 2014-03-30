# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        
        if head is None: return head
        
        tempHead = head #// Node for traversal
        while (tempHead is not None):
            if tempHead.next is None: return head
            if tempHead.val == tempHead.next.val:
                tempHead.next = tempHead.next.next
            else:
                tempHead = tempHead.next
            
        return head    
     
if __name__=="__main__" :
    
    class ListNode:
        def __init__(self, x):
            self.val = x
            self.next = None
        
    root=ListNode(1)
    a=ListNode(1)
    b=ListNode(2)
    c=ListNode(3)
    d=ListNode(3)
    root.next=b
    a.next=b
    b.next=c
    c.next=d
    result = Solution().deleteDuplicates(root)
    
    
    