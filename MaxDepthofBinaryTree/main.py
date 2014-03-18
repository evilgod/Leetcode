import MaxDepthofBinaryTree
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

root1=TreeNode(2)
root1.left=TreeNode(4)
root1.right=TreeNode(5)
root1.right.left=TreeNode(7)
root1.right.right=TreeNode(6)

result=MaxDepthofBinaryTree.Solution()
print result.maxDepth(root1)
