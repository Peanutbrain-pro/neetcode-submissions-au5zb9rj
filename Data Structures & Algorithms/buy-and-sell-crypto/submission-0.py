class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        smallest_till = prices[0]
        largest_diff = 0

        for p in prices[1:]:
            if p > smallest_till:
                if p - smallest_till > largest_diff:
                    largest_diff = p - smallest_till
            else:
                smallest_till = p

        return largest_diff