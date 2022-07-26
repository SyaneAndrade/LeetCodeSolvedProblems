# Definition for a binary tree node.
import math
from wsgiref import validate


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    

class Solution:
    def isValidBST(self, root) -> bool:
        return self.validate(root)
    
    def validate(self, node, high=math.inf, low=-math.inf):
        if not node:
            return True
            
        if node.val <= low or node.val >= high:
            return False
        
        return (self.validate(node.left, node.val, low) and 
                self.validate(node.right, high, node.val))
        


if __name__=='__main__':
    sol = Solution()
    tree_v = [5, 1, 4, None, None, 3, 6]

    root = TreeNode(tree_v[0], None, None)
    no = root

    no.left = TreeNode(tree_v[1], None, None)
    no.right = TreeNode(tree_v[2], None, None)
    no.right.left = TreeNode(tree_v[5], None, None)
    no.right.right = TreeNode(tree_v[6], None, None)

    isBST = sol.isValidBST(root)
    print(isBST)

    tree_s = [2,1,3]
    root2 = TreeNode(tree_s[0], None, None)
    no2 = root2

    no2.left = TreeNode(tree_s[1], None, None)
    no2.right = TreeNode(tree_s[2], None, None)

       
# no = no.left | 

    isBST2 = sol.isValidBST(root2)
    print(isBST2)