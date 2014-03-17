#Definition for a  binary tree node
#class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean

    def isSameTree(self, p, q):
        if p is None and q is None: return True
        if p is None or q is None: return False
        
    #    if (p is None and q is not None) or (p is not None and q is None): return False //can be simplify
    #    if p is None and q is None: return True
    #    if p.val != q.val:
    #        return False
        else:
    #        return True and (self.isSameTree(p.left, q.left)) and (self.isSameTree(p.right, q.right)) //can be simplify
            return (p.val==q.val) and (self.isSameTree(p.left, q.left)) and (self.isSameTree(p.right, q.right))
