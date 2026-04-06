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
    public ListNode reverseList(ListNode head) {
        ListNode ahead, middle, behind;
        if (head == null || head.next == null) {
            return head;
        }

        middle = head.next;
        behind = head;

        if (middle.next == null) {
            middle.next = behind;
            behind.next = null;
            return middle;
        }

        ahead = middle.next;
        behind.next = null;

        while (ahead != null) {
            middle.next = behind;
            behind = middle;
            middle = ahead;
            ahead = ahead.next;
        }

        middle.next = behind;
        return middle;
    }

}
