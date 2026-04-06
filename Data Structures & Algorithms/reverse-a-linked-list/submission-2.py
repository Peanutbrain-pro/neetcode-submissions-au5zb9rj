# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr1 = head
        if not head or not head.next:
            return head
        ptr2 = head.next
        
        while (ptr2.next != None):
            temp = ptr2.next
            ptr2.next = ptr1
            ptr1, ptr2 = ptr2, temp
        
        ptr2.next = ptr1

        head.next = None
        return ptr2