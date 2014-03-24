# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def __init__(self):
        self.A = []
    def inorderTraversal(self, root):
        
        if (root is not None):
            self.inorderTraversal(root.left)
            self.A.append(root.val)
            self.inorderTraversal(root.right)    
        return self.A 