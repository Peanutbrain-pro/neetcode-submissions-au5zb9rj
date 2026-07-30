class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = -float('inf')
        
        # forward pass
        curr = 1
        for n in nums:
            curr *= n
            if n == 0:
                max_prod = max(curr, max_prod)
                curr = 1
                continue
            max_prod = max(curr, max_prod)
        
        # backward pass
        curr = 1
        for n in nums[::-1]:
            curr *= n
            if n == 0:
                max_prod = max(curr, max_prod)
                curr = 1
                continue
            max_prod = max(curr, max_prod)

        return max_prod


            