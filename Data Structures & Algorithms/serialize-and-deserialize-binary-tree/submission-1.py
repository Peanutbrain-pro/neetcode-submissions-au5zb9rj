# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        nodes = collections.deque()
        stack = collections.deque()
        stack.append(root)
        while stack:
            curr = stack.pop()
            if not curr:
                nodes.append('null')
                continue
            nodes.append(str(curr.val))
                
            stack.append(curr.right)
            stack.append(curr.left)
            
        print("stack: ", stack, "\tnodes: ", nodes)
        return ",".join(nodes)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        nodes = data.split(",")
        if nodes[0] == "null":
            return

        index = [0]
        def dfs(index, nodes):
            if index[0] >= len(nodes) or nodes[index[0]] == 'null':
                return
            
            nt = TreeNode(int(nodes[index[0]]))
            index[0] += 1
            nt.left = dfs(index, nodes)
            index[0] += 1
            nt.right = dfs(index, nodes)

            return nt

        return dfs(index, nodes)


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))