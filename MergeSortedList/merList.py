class Solution:
    
    def mergelist(self, l1, l2):
        
        pa=l1
        pb=l2
        if l1 is None: return l2 
        if l2 is None: return l1
        
        if l1.val >= l2.val:
            root=pb
        else:
            root=pa
        
        temp1 = None
        
        while (pa is not None) and (pb is not None):
            if pb.val <= pa.val:
                if temp1 is not None: temp1.next=pb
                temp=pb
                pb=pb.next
                temp.next=pa
                temp1=temp
            elif pa.next is None:
                pa.next=pb
                return root
            else:
                temp1=pa
                pa=pa.next
        return root

if __name__=="__main__":
    
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
    
    result= Solution().mergelist(d, a)
    while result is not None:
        print result.val
        result=result.next