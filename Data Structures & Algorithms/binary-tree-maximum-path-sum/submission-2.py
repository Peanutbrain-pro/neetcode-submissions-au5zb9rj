# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        greatest_max_sum = [float('-inf')]

        def traverse(node, greatest_max_sum):
            max_sum = node.val
            max_branch = node.val
            temp_mb = 0
            if node.left:
                mb = traverse(node.left, greatest_max_sum)
                if mb > temp_mb:
                    temp_mb = mb
                if mb > 0:
                    max_sum += mb
            
            if node.right:
                mb = traverse(node.right, greatest_max_sum)
                if mb > temp_mb:
                    temp_mb = mb
                if mb > 0:
                    max_sum += mb

            max_branch += temp_mb

            if max_sum > greatest_max_sum[0]:
                greatest_max_sum[0] = max_sum

            return max_branch

        traverse(root, greatest_max_sum)
        return greatest_max_sum[0]
        
