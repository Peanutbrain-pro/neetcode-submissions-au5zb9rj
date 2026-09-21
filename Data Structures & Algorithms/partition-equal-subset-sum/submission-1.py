class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False

        half = total / 2
        
        def recur(index, capacity):
            print("index: ", index, "\tcapacity: ", capacity)
            if index >= len(nums):
                return False
            if capacity == nums[index]:
                return True
            
            if capacity > 0 and recur(index + 1, capacity - nums[index]):
                return True
            else:
                return recur(index + 1, capacity)

        return recur(0, half)