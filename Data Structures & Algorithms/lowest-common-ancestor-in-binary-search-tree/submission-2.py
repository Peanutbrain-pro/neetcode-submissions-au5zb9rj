# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p is q:
            return p
        
        stack = collections.deque()

        # get stack for p
        def createStack(node, target_node, stack):
            if not node:
                return
            if node.val == target_node.val:
                stack.append((node, 0))
                return

            if node.val > target_node.val:
                stack.append((node, -1))
                createStack(node.left, target_node, stack)
            else:
                stack.append((node, 1))
                createStack(node.right, target_node, stack)
        
        createStack(root, p, stack)

        for node, dir in stack:
            if dir == -1:
                if node.val <= q.val:
                    # This is where it diverts
                    return node
            elif dir == 1:
                if node.val >= q.val:
                    return node
            else:
                return node
        print("This shouldn't reach here")