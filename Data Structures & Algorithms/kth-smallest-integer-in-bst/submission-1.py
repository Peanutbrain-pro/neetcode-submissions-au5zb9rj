# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = [0]

        def dfs(node, n_array, k):
            if node is None:
                return

            left = dfs(node.left, n_array, k)
            if left is not None:
                return left 

            n_array[0] += 1
            if n_array[0] == k:
                return node.val
            
            right = dfs(node.right, n_array, k)
            if right is not None:
                return right

        return dfs(root, n, k)      
            
