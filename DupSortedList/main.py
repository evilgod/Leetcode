import dupsorted
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

root=ListNode(1)
root.next=ListNode(1)
root.next.next=ListNode(2)
root.next.next.next=ListNode(3)
root.next.next.next.next=ListNode(3)
#===============================================================================

#print root
result = dupsorted.Solution()

#print result.deleteDuplicates(root)