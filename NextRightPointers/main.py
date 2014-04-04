import connectNode

class TreeNode:
        def __init__(self, x):
            self.val = x
            self.right = None
            self.left = None
            self.next = None
            
root = TreeNode(1)
root.right=TreeNode(2)
root.left=TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
result = connectNode.Solution()
result.connect(root)