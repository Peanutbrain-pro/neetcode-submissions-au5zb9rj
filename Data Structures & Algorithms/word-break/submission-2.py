class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        dp = [False] * len(s)
        dp.append(True)
        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                # print(s[i:], word)
                if s[i:].startswith(word):
                    # print(word, s[i:], i+ len(word))
                    if dp[i + len(word)]:
                        dp[i] = True
            print(dp)
        
        return dp[0]
            