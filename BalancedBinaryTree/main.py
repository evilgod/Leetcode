import balanced
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

root1=TreeNode(2)
root1.left=TreeNode(4)
root1.right=TreeNode(5)
root1.right.right=TreeNode(6)
root1.right.right.right=TreeNode(7)
result=balanced.Solution()
print result.isBalanced(root1)
