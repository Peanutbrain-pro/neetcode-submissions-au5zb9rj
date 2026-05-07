class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def dfs(available, comb):
            if len(available) == 1:
                comb.append(nums[available[0]])
                result.append(comb.copy())
                comb.pop()
                return

            for i in available:
                comb.append(nums[i])
                temp = available.copy()
                temp.remove(i)
                dfs(temp, comb)
                comb.pop()

        dfs([i for i in range(len(nums))], [])
        return result