/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        if (lists.length == 0) {
            return null;
        }

        ListNode head = lists[0], curr, l1, l2;
        for (int i = 1; i < lists.length; i++) {
            l1 = head;
            l2 = lists[i];

            if (l2 == null) {
                continue;
            }
            if (l1 == null) {
                head = l2;
                continue;
            }

            // for the first elements
            if (l1.val <= l2.val) {
                curr = l1;
                l1 = l1.next;
            } else {
                curr = l2;
                head = curr;
                l2 = l2.next;
            }

            while (l1 != null && l2 != null) {
                if (l1.val <= l2.val) {
                    curr.next = l1;
                    l1 = l1.next;
                } else {
                    curr.next = l2;
                    l2 = l2.next;
                }
                curr = curr.next;
            }

            if (l1 == null) {
                curr.next = l2;
            } else {
                curr.next = l1;
            }
        }

        return head;
    }
}
