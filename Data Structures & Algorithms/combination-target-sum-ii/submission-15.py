class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        result = []
        candidates.sort()

        def dfs(i, comb, total):
            # print(i, comb, total)
            if total == target:
                # print("founc: ", comb)
                # c = tuple(sorted(comb))
                result.append(comb.copy())
                # result.append(comb.copy())
                return
            if total > target or i == len(candidates):
                # print("too large or i == len(candidates)")
                return
            
            # if (i + 1) < len(candidates):
            comb.append(candidates[i])
            dfs(i + 1, comb, total + candidates[i])
            comb.pop()
            x = i + 1
            while x < len(candidates) and (candidates[x] == candidates[i]):
                x += 1
            dfs(x, comb, total)
            

        dfs(0, [], 0)
        # return [list(t) for t in result]
        return result