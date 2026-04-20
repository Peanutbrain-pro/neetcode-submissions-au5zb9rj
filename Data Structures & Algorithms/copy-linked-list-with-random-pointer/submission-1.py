"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        # 3 7 4 5 null
        # 0 1 2 3
        # n 5 3
        #
        if not head:
            return None


        ptr_index_dict = {}
        # random_indices = deque()
        i = 0

        new_head = Node(head.val)
        ptr_index_dict[head] = i
        optr = head
        nptr = new_head
        new_index_ptr_dict = {i: new_head}

        while optr.next:
            i += 1
            optr = optr.next
            ptr_index_dict[optr] = i
            nptr.next = Node(optr.val)
            nptr = nptr.next
            new_index_ptr_dict[i] = nptr 

        optr = head
        nptr = new_head
        i = 0
        while optr:
            nptr.random = new_index_ptr_dict[ptr_index_dict[optr.random]] if optr.random else None

            nptr = nptr.next
            optr = optr.next

        return new_head
