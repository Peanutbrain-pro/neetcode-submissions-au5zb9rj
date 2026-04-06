class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict()

        for i, num in enumerate(nums):
            required_num = target - num
            if required_num in hashmap:
                return [hashmap[required_num], i]
            else:
                hashmap[num] = i
