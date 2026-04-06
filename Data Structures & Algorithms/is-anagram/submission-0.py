class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count_s, count_t = {}, {}

        for i in range(len(s)):
            if s[i] in count_s:
                count_s[s[i]] += 1
            else:
                count_s[s[i]] = 1

            if t[i] in count_t:
                count_t[t[i]] += 1
            else:
                count_t[t[i]] = 1

        # for key in count_s:
        #     if key not in count_t:
        #         return False
        #     elif count_t[key] != count_s[key]:
        #         return False
        if count_s != count_t:
            return False
        return True
        