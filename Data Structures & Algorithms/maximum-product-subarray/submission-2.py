class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = -float('inf')
        
        # forward pass
        # prefix = 2
        curr = 1
        for n in nums:
            curr *= n
            if n == 0:
                # prefix = 1
                max_prod = max(curr, max_prod)
                curr = 1
                continue
            max_prod = max(curr, max_prod)
        #max_prod = max(max_prod, curr)

        # backward pass
        # suffix = 1
        curr = 1
        for n in nums[::-1]:
            curr *= n
            if n == 0:
                # suffix = 1
                max_prod = max(curr, max_prod)
                curr = 1
                continue
            max_prod = max(curr, max_prod)
        #max_prod = max(max_prod, curr)

        return max_prod


            