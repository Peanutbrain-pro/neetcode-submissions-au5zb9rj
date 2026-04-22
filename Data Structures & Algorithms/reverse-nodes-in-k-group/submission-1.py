# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head

        if head == None:
            return head

        new_head = ListNode()
        new_head.next = head
        before_start = new_head
        end = new_head
        while before_start:
            # before_start = end
            end = before_start
            count = 0
            while count < k and end.next:
                end = end.next
                count += 1
            if count < k:
                return new_head.next

            left, mid, right = (
                before_start.next,
                before_start.next.next,
                before_start.next.next.next,
            )
            while right != end.next:
                mid.next = left
                left = mid
                mid = right
                right = right.next
            mid.next = left

            temp = before_start.next
            before_start.next.next = right
            before_start.next = end
            before_start = temp

        return new_head.next
