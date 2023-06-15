# #Time Complexity : O(n) / O(2^l) l: Level/height of the tree
# #Space complexity : O(l) Most number of elements in recursive stack at one moment
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.prev = None
        self.flag = True  # Initialize flag as True
        self.inorder(root)
        return self.flag
    
    def inorder(self, root: Optional[TreeNode]) -> None:
        if root is None:
            return
        self.inorder(root.left)
        if self.prev is not None and self.prev.val >= root.val:
            self.flag = False
        self.prev = root
        self.inorder(root.right)
        print("up")
        print(root.val)

# Create the binary search tree from the list
root = TreeNode(100)
root.left = TreeNode(50)
root.right = TreeNode(150)
root.left.left = TreeNode(20)
root.left.right = TreeNode(80)
root.right.left = TreeNode(120)
root.right.right = TreeNode(180)
root.left.left.left = TreeNode(10)
root.left.left.right = TreeNode(40)
root.left.right.left = TreeNode(75)
root.left.right.right = TreeNode(90)
root.right.left.left = TreeNode(110)
root.right.left.right = TreeNode(140)
root.right.right.left = TreeNode(160)
root.right.right.right = TreeNode(200)

s = Solution()
print(s.isValidBST(root))  # Output: True
