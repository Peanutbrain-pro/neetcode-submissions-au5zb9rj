class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1 or s == s[::-1]:
            return s

        longest = 1
        # longestring = ""
        longestStringIndices = (0, 0)

        for i in range(len(s)):
            # odd check
            l, r = i, i
            # print("Center: ", l, r)
            while l >= 0 and r < len(s):
                # print("l: ", l, "r: ", r)
                if s[l] == s[r]:
                    if (r - l + 1) > longest:
                        longest = r - l + 1
                        longestStringIndices = (l, r)
                else:
                    break
                l -= 1
                r += 1
            
            # even check
            l, r = i, i+1
            # print("Center: ", l, r)
            while l >= 0 and r < len(s):
                # print("l: ", l, "r: ", r)
                if s[l] == s[r]:
                    if (r - l + 1) > longest:
                        longest = r - l + 1
                        longestStringIndices = (l, r)
                else:
                    break
                l -= 1
                r += 1
                
        return s[longestStringIndices[0]: longestStringIndices[1] + 1]