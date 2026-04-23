# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        traversed = []

        def dfs(root, level, traversed):
            if root is None:
                return
            
            if len(traversed) <= level:
                traversed.append([root.val])
            else:
                traversed[level].append(root.val)
            
            dfs(root.left, level + 1, traversed)
            dfs(root.right, level + 1, traversed)

        dfs(root, 0, traversed)
        return traversed