class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        carry = 0

        l1_ptr = l1
        l2_ptr = l2
        new_val_head = ListNode()
        new_ptr = new_val_head
        while l1_ptr and l2_ptr:
            carry, r = divmod(l1_ptr.val + l2_ptr.val + carry, 10)
            new_ptr.next = ListNode()
            new_ptr = new_ptr.next
            new_ptr.val = r

            l1_ptr = l1_ptr.next
            l2_ptr = l2_ptr.next

        if l1_ptr:
            while l1_ptr:
                carry, r = divmod(l1_ptr.val + carry, 10)
                new_ptr.next = ListNode()
                new_ptr = new_ptr.next
                new_ptr.val = r

                l1_ptr = l1_ptr.next

        if l2_ptr:
            while l2_ptr:
                carry, r = divmod(l2_ptr.val + carry, 10)
                new_ptr.next = ListNode()
                new_ptr = new_ptr.next
                new_ptr.val = r

                l2_ptr = l2_ptr.next

        if carry != 0:
            new_ptr.next = ListNode()
            new_ptr.next.val = carry

        return new_val_head.next