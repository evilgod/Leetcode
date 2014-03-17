# Definition for a  binary tree node
#class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None         
#        self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        
        if root is None:
            return 0
        
        #if self.maxDepth(root.left) >= self.maxDepth(root.right):
        #   return self.maxDepth(root.left) + 1
        
        else:
            return max(self.maxDepth(root.right) + 1, self.maxDepth(root.left) + 1)
            #return self.maxDepth(root.right) + 1 (Time Limit Exceeded)
