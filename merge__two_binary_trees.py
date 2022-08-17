# Definition for a binary tree node.
from hashlib import new


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if root1 is None:
            return root2
        if root2 is None:
            return root1
        new_root = TreeNode(root1.val + root2.val)
        new_root.left = self.mergeTrees(root1.left, root2.left)
        new_root.right = self.mergeTrees(root1.right, root2.right)
        return new_root
    

sol = Solution()

root1 = [1,3,2,5]
root2 = [2,1,3,None,4,None,7]

root1 = TreeNode(1)
root2 = TreeNode(2)

root1.left = TreeNode(3)
root1.right = TreeNode(2)
root1.left.left = TreeNode(5)

root2.left = TreeNode(1)
root2.right = TreeNode(3)
root2.left.right = TreeNode(4)
root2.right.right = TreeNode(7)

new_root = sol.mergeTrees(root1, root2)

print(new_root.val)