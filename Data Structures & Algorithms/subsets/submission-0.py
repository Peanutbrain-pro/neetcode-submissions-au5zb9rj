class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        for n in nums:
            result.append([n])
            for x in result[:-1]:
                result.append([n] + x)

        result.insert(0, [])
        return result
