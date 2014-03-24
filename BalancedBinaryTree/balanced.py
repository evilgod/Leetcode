class Solution:
    
    
    
    def maxDepth(self, root):
        
        if root is None:
            return 0
        
        #if self.maxDepth(root.left) >= self.maxDepth(root.right):
        #   return self.maxDepth(root.left) + 1
        
        else:
            return max(self.maxDepth(root.right) + 1, self.maxDepth(root.left) + 1)
    
    
    def isBalanced(self, root):
        if root is None:
            return True
        if abs(self.maxDepth(root.right)-self.maxDepth(root.left))>1:
            return False
        else:
            return self.isBalanced(root.right) and self.isBalanced(root.left) 
            
        
    
        