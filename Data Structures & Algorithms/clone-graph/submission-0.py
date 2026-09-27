"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return

        # get the nodes mapped to real ones
        hash = {}
        visited = set()
        stack = [node]
        while stack:
            n = stack.pop()
            newNode = Node(n.val)
            hash[n] = newNode
            visited.add(n)
            stack.extend(x for x in n.neighbors if x not in visited)
        # print(hash)

        # join them according to their neighbours
        for key in hash:
            n = hash[key]
            newNeighbors = [hash[k] for k in key.neighbors]
            n.neighbors = newNeighbors

        return hash[node]

