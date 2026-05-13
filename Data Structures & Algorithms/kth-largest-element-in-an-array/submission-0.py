class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minheap = []

        for i in range(len(nums)):
            if len(minheap) < k:
                heapq.heappush(minheap, nums[i])
                continue

            if nums[i] <= minheap[0]:
                continue

            heapq.heappushpop(minheap, nums[i])
        
        return minheap[0]
            
