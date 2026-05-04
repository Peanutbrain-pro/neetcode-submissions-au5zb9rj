# Not accurate right now

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums:
            return []

        # n = sorted(nums)
        result = []

        def dfs(i, comb, total):
            # print(i, comb, total)
            if total > target or i == len(nums):
                return
            if total == target:
                result.append(comb.copy())
                # comb.pop()
                return

            comb.append(nums[i])
            dfs(i, comb, total + nums[i])
            comb.pop()
            dfs(i+1, comb, total)

        dfs(0, [], 0)

        return result
                