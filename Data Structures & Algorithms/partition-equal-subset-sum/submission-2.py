class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False

        half = total / 2
        hash = {}
        def recur(index, capacity):
            if (index, capacity) in hash:
                return hash[(index, capacity)]

            # print("index: ", index, "\tcapacity: ", capacity)
            if index >= len(nums):
                hash[(index, capacity)] = False
                return False
            if capacity == nums[index]:
                hash[(index, capacity)] = True
                return True
            
            if capacity > 0 and recur(index + 1, capacity - nums[index]):
                return True
            else:
                hash[(index + 1, capacity - nums[index])] = False
                if recur(index + 1, capacity):
                    return True
                else:
                    hash[(index + 1, capacity)] = False
                    return False

        return recur(0, half)
