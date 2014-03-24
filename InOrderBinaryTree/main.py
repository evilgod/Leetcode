import inorder

class TreeNode:
        def __init__(self, x):
            self.val = x
            self.right = None
            self.left = None
            
root=TreeNode(5)
root.right=TreeNode(10)
root.left=TreeNode(3)
root.right.right=TreeNode(20)
root.right.right.left=TreeNode(13)
root.right.right.right=TreeNode(25)
result = inorder.Solution()
print result.inorderTraversal(root)