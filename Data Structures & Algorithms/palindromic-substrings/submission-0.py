class Solution:
    def countSubstrings(self, s: str) -> int:
        if len(s) == 1:
            return 1

        n = 0

        for i in range(len(s)):
            # odd palindromes
            l, r = i, i
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    n += 1
                else:
                    break
                l -= 1
                r += 1

            # even palindromes
            l, r = i, i+1
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    n += 1
                else:
                    break
                l -= 1
                r += 1
        
        return n