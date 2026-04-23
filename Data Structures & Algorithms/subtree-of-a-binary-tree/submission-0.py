# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot is None:
            return True
        
        def checkSameSubtree(root, subroot):
            if root is None:
                if subroot is None:
                    return True
                else:
                    return False
            else:
                if subroot is None:
                    return False
            
            if root.val != subroot.val:
                return False
            else:
                left_same = checkSameSubtree(root.left, subroot.left)
                right_same = checkSameSubtree(root.right, subroot.right)
                if left_same and right_same:
                    return True
                else:
                    return False

        def dfs(root_node, subroot):
            if root_node is None:
                return False
            same = checkSameSubtree(root_node, subroot)
            if not same:
                if dfs(root_node.left, subroot):
                    return True
                elif dfs(root_node.right, subroot):
                    return True
                else:
                    return False
            else:
                return True

        return dfs(root, subRoot)