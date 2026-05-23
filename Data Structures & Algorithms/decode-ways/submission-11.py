class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0

        hashset = {len(s): 1}

        def dfs(index):
            if index in hashset:
                return hashset[index]
            if s[index] == '0':
                return 0

            res = dfs(index + 1)
            if (index + 1) < len(s):
                if s[index] == "1" or (s[index] == "2" and s[index+1] in "0123456"):
                    res += dfs(index + 2)
                
            hashset[index] = res
            return res

        return dfs(0)
