class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        digitLetters = ["", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        result = []
        n = len(digits)
        def dfs(i, comb):
            if i == n:
                result.append("".join(comb))
                return

            letters = digitLetters[int(digits[i]) - 1]
            for l in letters:
                comb.append(l)
                dfs(i+1, comb)
                comb.pop()

        dfs(0, [])
        return result