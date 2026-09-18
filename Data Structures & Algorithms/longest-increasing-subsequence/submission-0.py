class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        larger = [0] * len(nums)
        for ni in range(len(nums) - 1, -1, -1):
            for li in range(ni + 1, len(nums)):
                if nums[li] > nums[ni]:
                    larger[ni] = max(larger[ni], larger[li] + 1)
        
        return max(larger) + 1