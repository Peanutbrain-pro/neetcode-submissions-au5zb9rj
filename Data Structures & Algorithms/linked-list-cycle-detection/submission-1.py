# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        index = 0
        visited = set()
        node = head

        while node.next:
            if node in visited:
                return True
            visited.add(node)
            node = node.next
            index += 1
        return False