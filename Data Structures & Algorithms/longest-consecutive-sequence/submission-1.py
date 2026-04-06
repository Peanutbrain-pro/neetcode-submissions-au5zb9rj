class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lcs = 0
        num_set = set(nums)

        for n in num_set:
            if n - 1 not in num_set:
                cs = 1
                i = 1
                while n + i in num_set:
                    cs += 1
                    i += 1
                if cs > lcs:
                    lcs = cs

        return lcs