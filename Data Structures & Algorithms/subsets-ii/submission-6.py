class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        hash_set = set()
        result = []
        for i in nums:
            print(i, hash_set)
            added = False
            if (i,) not in hash_set:
                hash_set.add((i,))
                result.append([i])
                added = True

            print("result before: ", result)
            # new_list = list(result)[:-1] if added else list(result)
            new_list = result[:-1] if added else result[:]
            print("newList after: ", new_list)
            for r in new_list:
                sorted_comb = sorted([i] + r)
                t = tuple(sorted_comb)
                if t not in hash_set:
                    hash_set.add(t)
                    result.append(sorted_comb)

        result.append([])
        return result