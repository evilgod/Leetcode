import sametree
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

root1=TreeNode(2)
root1.left=TreeNode(4)
root1.right=TreeNode(5)
root1.right.right=TreeNode(6)
root1.right.left=TreeNode(7)

root2=TreeNode(2)
root2.left=TreeNode(4)
root2.right=TreeNode(5)
root2.right.right=TreeNode(6)
root2.right.left=TreeNode(7)

result=sametree.Solution()
print result.isSameTree(root1, root2)
