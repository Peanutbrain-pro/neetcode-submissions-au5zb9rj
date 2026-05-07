class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return

        result = []

        def dfs(comb, nLeftBrace, nRightBrace):
            if nLeftBrace == nRightBrace == n:
                result.append("".join(comb))
                return

            if nLeftBrace < n:
                comb.append('(')
                dfs(comb, nLeftBrace + 1, nRightBrace)
                comb.pop()
            
            if nLeftBrace > nRightBrace:
                comb.append(')')
                dfs(comb, nLeftBrace, nRightBrace + 1)
                comb.pop()

        dfs([], 0, 0)
        return result
