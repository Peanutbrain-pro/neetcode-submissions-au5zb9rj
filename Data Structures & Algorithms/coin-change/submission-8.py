class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        coins.sort()
        
        self.dp = [float('inf')] * (amount + 1)
        self.dp[0] = 0

        for i in range(1, amount + 1):
            smallest = float('inf')

            for c in coins:
                if (i - c) == 0:
                    smallest = 1
                    break
                
                if (i - c) < 0:
                    break

                steps = self.dp[i - c] + 1
                if steps == 0:
                    continue
                smallest = min(steps, smallest)

            if smallest == float('inf'):
                self.dp[i] = -1
            else:
                self.dp[i] = smallest
            # print(self.dp)

        return self.dp[-1]
