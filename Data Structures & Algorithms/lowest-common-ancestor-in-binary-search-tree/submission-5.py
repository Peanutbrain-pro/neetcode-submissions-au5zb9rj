# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        ptr = root
        while ptr:
            if p.val < ptr.val and q.val < ptr.val:
                ptr = ptr.left
            elif p.val > ptr.val and q.val > ptr.val:
                ptr = ptr.right
            else:
                return ptr
        