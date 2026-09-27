class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False

        half = total // 2
        dp = [False] * (half + 1)
        dp[0] = True

        for n in nums:
            for i in range(len(dp) - 1, n - 1, -1):
                if dp[i - n] == True:
                    dp[i] = True
            if dp[-1]:
                return True

        return False
            