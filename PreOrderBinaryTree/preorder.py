
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
    def preorderTraversal(self, root):
        
        if (root is not None):
            self.A.append(root.val)
            self.preorderTraversal(root.left)
            self.preorderTraversal(root.right)    
        return self.A    

#===============================================================================
# if __name__=="__main__":
#     
#     class TreeNode:
#         def __init__(self, x):
#             self.val = x
#             self.right = None
#             self.left = None
#             
#     root=TreeNode(5)
#     root.right=TreeNode(10)
#     root.left=TreeNode(3)
#     root.right.right=TreeNode(20)
#     root.right.right.left=TreeNode(13)
#     root.right.right.right=TreeNode(25)
#     print Solution().preorderTraversal(root)
#===============================================================================