class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        # take only the left partition

        def dfs(left, right, comb):
            # print(left, right, s[left: right+1], comb)
            if not self.isPalindrome(s[left: right+1]):
                return

            comb.append(s[left: right+1])
            if right == len(s) - 1:
                # this selection is at the end
                result.append(comb.copy())
                comb.pop()
                return

            # Not at the end
            for newRight in range(right+1, len(s)):
                dfs(right+1, newRight, comb)
                
            comb.pop()

        temp = []
        for i in range(len(s)):
            dfs(0, i, temp)
        return result
    
    def isPalindrome(self, s):
        return s == s[::-1]