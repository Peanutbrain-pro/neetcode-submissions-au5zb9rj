# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0
        self.getHeight(root)
        return self.max_diameter
    def getHeight(self, root):
        if root is None:
            return 0
        left_height = 1 + self.getHeight(root.left)
        right_height = 1 + self.getHeight(root.right)
        if left_height + right_height - 2 > self.max_diameter:
            self.max_diameter = left_height + right_height - 2
        return max(left_height, right_height)


