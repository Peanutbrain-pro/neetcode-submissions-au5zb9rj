# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # count = 1

        def dfs(root, count, max_yet):
            count = 0
            if root is None:
                return 0

            if root.val >= max_yet:
                count = 1
                max_yet = root.val
            
            return dfs(root.left, count, max_yet) + dfs(root.right, count, max_yet) + count

        return dfs(root, 0, float('-inf'))