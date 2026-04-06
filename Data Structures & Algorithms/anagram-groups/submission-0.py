class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = dict()

        for string in strs:
            freq = [0]*26
            for char in string:
                freq[ord(char) - ord('a')] += 1
            newkey = tuple(freq)

            if newkey not in hashmap:
                hashmap[newkey] = [string]
            else:
                hashmap[newkey].append(string)
        
        result = list(hashmap.values())
        return result