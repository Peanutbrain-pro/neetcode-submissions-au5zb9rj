class Solution:
    def findMin(self, nums: List[int]) -> int:
        result = nums[0]

        l = 0
        h = len(nums) - 1

        while h >= l:
            mid = l + (h - l) // 2

            if nums[l] <= nums[mid]:
                result = min(result, nums[l])
                l = mid + 1

            else:
                result = min(result, nums[mid])
                h = mid - 1

        return result