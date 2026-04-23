# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def isValid(node, greaterThan, lessThan):
            if node is None:
                return True
            print("node: ", node.val)

            if node.left:
                print("node.left: ", node.left.val)
                if node.left.val >= node.val or node.left.val <= greaterThan:
                    print(node.left.val, ">=", node.val)
                    return False

            if node.right:
                print("node.right: ", node.right.val)
                if node.right.val <= node.val or node.right.val >= lessThan:
                    print(node.right.val, "<=", node.val)
                    return False

            print()
            return isValid(node.left, lessThan = node.val, greaterThan = greaterThan) and isValid(
                node.right, greaterThan = node.val, lessThan = lessThan
            )

        return isValid(root, greaterThan = float('-inf'), lessThan = float('inf'))
