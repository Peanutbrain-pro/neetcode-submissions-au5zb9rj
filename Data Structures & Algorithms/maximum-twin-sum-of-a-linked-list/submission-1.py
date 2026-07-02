# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # 0 1 2 3 4 5 6 7 8

        length = 0
        ptr = head
        while ptr:
            length += 1
            ptr = ptr.next
        # print(length)

            
        sums = []
        ptr = head
        i = 0
        while i < int(length / 2):
            # print(i, ptr.val, sums)
            sums.append(ptr.val)
            ptr = ptr.next
            i += 1
        
        # print("Now opposite way")
        i = -1
        while i >= - int(length / 2):
            # print(i, ptr.val, sums)
            sums[i] += ptr.val
            ptr = ptr.next
            i -= 1

        return max(sums)