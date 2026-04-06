# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if head is None or head.next is None:
            return

        buffer = ListNode()
        buffer.next = head

        end = buffer
        for i in range(n):
            end = end.next

        switch = buffer

        while end.next:
            end = end.next
            switch = switch.next

        temp = switch.next
        switch.next = switch.next.next
        if switch == buffer:
            head = switch.next

        # printing the linked list
        # node = head
        # while node:
        #     print(node.val, end="->")
        #     node = node.next

        # return temp


        return head

