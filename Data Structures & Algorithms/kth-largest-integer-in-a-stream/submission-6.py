
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums

        # heapifying nums
        for i in range(len(nums) - 1, -1, -1):
            self.heapify(i)

        print("Heapified before: ", self.nums)
        # Only keeping the first k largest elements by removing the smallest elements
        # the smallest one from the remaining is the kth largest element
        for i in range(len(nums) - k):
            self.nums[0] = self.nums[-1]
            self.nums.pop()
            self.heapify(0)

        print("Heapified: ", self.nums)

    def add(self, val: int) -> int:
        if len(self.nums) < self.k:
            self.nums.append(val)
            self.upheapify(self.k-1)
            return self.nums[0]

        if val <= self.nums[0]:
            return self.nums[0]

        self.nums[0] = val
        self.heapify(0)

        print("Heap before returning kth largest: ", self.nums)
        return self.nums[0]

    def heapify(self, index):
        left = index * 2 + 1
        right = index * 2 + 2
        length = len(self.nums)

        smallest_child = None
        if left < length:
            if self.nums[left] < self.nums[index]:
                smallest_child = left
            if right < length:
                if self.nums[right] < self.nums[index] and self.nums[right] < self.nums[left]:
                    smallest_child = right

        if smallest_child:
            self.nums[index], self.nums[smallest_child] = self.nums[smallest_child], self.nums[index]
            self.heapify(smallest_child)

    def upheapify(self, index):
        if index == 0:
            return

        if index % 2:
            p = (index - 1) // 2
        else:
            p = (index - 2) // 2

        if self.nums[index] < self.nums[p]:
            self.nums[index], self.nums[p] = self.nums[p], self.nums[index]
            self.upheapify(p)
        