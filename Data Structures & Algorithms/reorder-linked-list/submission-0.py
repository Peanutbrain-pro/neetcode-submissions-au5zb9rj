class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        if not head or not head.next or not head.next.next:
            return

        s = head
        f = head.next

        # slow fast pointers to reach the half of the linked list
        while f and f.next:
            s = s.next
            f = f.next.next

        h2 = s.next
        s.next = None
        # print("Found starting of 2nd list: ", h2.val)

        # Reversing the second half of the linked list
        if h2.next is None:
            pass
        else:
            nxt = h2.next
            nxtnxt = nxt.next
            h2.next = None

            # print(h2.val)
            # print(nxt.val)

            while nxtnxt:
                nxt.next = h2
                h2 = nxt
                nxt = nxtnxt
                nxtnxt = nxtnxt.next
            nxt.next = h2
            h2 = nxt

        # # Printing Linked lists
        # node1, node2 = head, h2
        # print("Head of node 1 = ", node1.val, "Head of node 2 = ", node2.val)
        # while node1:
        #     print(node1.val, end="->")
        #     node1 = node1.next
        # print()
        # while node2:
        #     print(node2.val, end="->")
        #     node2 = node2.next
        # print()

        # Merging the two linked lists
        node1, node2 = head, h2
        while node2:
            temp1 = node1.next
            temp2 = node2.next

            node1.next = node2
            node2.next = temp1
            node1 = temp1
            node2 = temp2

        # node1 = head
        # while node1:
        #     print(node1.val, end="->")
        #     node1 = node1.next
        #     sleep(0.1)
        # print()
