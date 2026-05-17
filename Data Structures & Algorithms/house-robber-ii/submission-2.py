class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return max(nums)

        nums2 = nums.copy()
        nums2[1] = max(nums2[0], nums2[1])
        # including first
        for i in range(2, len(nums) - 1):
            nums2[i] = max(nums2[i] + nums2[i - 2], nums2[i - 1])

        # not including first
        nums[2] = max(nums[1], nums[2])
        for i in range(3, len(nums)):
            nums[i] = max(nums[i] + nums[i - 2], nums[i - 1])

        return max(nums[-1], nums2[-2])
