class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_heap = []
        for i in range(k):
            heapq.heappush(max_heap, -nums[i])
        maximum = -max_heap[0]
        output = [maximum]

        for i in range(k, len(nums)):
            max_heap.remove(-nums[i-k])
            max_heap.append(-nums[i])
            heapq.heapify(max_heap)
            output.append(-max_heap[0])
        
        return output