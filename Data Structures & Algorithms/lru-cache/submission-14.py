class ListNode:
    def __init__(self, key=None, value=None, next=None) -> None:
        self.key: int | None = key
        self.val: int | None = value
        self.next: ListNode | None = next


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.count = 0
        self.head = ListNode()
        self.end = self.head
        self.back_hash = {}

    def get(self, key: int) -> int:
        if key in self.back_hash:
            left = self.back_hash[key]
            if left.next != self.end:
                self.put_node_to_end(left.next)
            return self.end.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.back_hash:
            if self.count < self.capacity:
                self.count += 1
            else:
                del self.back_hash[self.head.next.key]

                if self.head.next.next:
                    self.back_hash[self.head.next.next.key] = self.head
                    self.head.next = self.head.next.next
                else:
                    self.head.next = None
                    self.end = self.head

            self.end.next = ListNode(key, value)
            self.back_hash[key] = self.end
            self.end = self.end.next
        else:
            left = self.back_hash[key]
            if left.next != self.end:
                self.put_node_to_end(left.next)
            self.end.val = value

    def put_node_to_end(self, node):
        left = self.back_hash[node.key]
        left.next = node.next
        self.back_hash[node.next.key] = left
        self.end.next = node
        self.back_hash[node.key] = self.end
        node.next = None
        self.end = node
