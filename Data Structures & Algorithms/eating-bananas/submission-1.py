import math


class Solution:
    def time_taken_hrs(self, piles, k):
        time = 0
        for bananas in piles:
            time += math.ceil(bananas / k)
        # print("Time taken for ", k, " = ", time)
        return time

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        lowest_k = high

        while low <= high:
            # print(f"low: {low}   high: {high}")
            mid = (low + high) // 2
            time_taken = self.time_taken_hrs(piles, mid)

            if time_taken > h:
                low = mid + 1
            else:
                lowest_k = mid
                high = mid - 1

        return lowest_k
