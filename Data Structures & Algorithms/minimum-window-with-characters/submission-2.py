class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # print("\n\n\n")
        t_freq = {}
        for c in t:
            t_freq[c] = t_freq.get(c, 0) + 1

        # print("T frequency: \n", t_freq)
        s_freq = {}
        shortest_window = None
        l = 0
        r = 0
        while r < len(s) and l < len(s):
            # print("left: ", l, "right: ", r, s[l : r + 1])
            if s[l] not in t_freq:
                # print(s[l], "not in t")
                l += 1
                continue

            if s[r] not in t_freq:
                # print(s[r], "not in t")
                r += 1
                continue

            s_freq[s[r]] = s_freq.get(s[r], 0) + 1
            # print(s_freq)

            if s_freq[s[l]] > t_freq[s[l]]:
                s_freq[s[l]] -= 1
                l += 1
                s_freq[s[r]] -= 1
                continue

            if s_freq[s[r]] > t_freq[s[r]]:
                # print("s has more frequency of ", s[r], "than t")
                if s[r] == s[l]:
                    s_freq[s[l]] -= 1
                    l += 1
                    # print("we can remove the left few chars")
                    s_freq[s[r]] -= 1
                    continue

            all_char_present = True
            for key in t_freq:
                if key not in s_freq or s_freq[key] < t_freq[key]:
                    # print("s still needs to find more characters from t")
                    r += 1
                    all_char_present = False
                    break
            if not all_char_present:
                continue

            # print("FOUND A MATCH:", s[l : r + 1])
            # all characters from t are present with required frequency in this substring
            if shortest_window is None or (r - l) < (
                shortest_window[1] - shortest_window[0]
            ):
                shortest_window = (l, r)

            # check for new substrings
            s_freq[s[l]] -= 1
            l += 1
            r += 1

        return (
            s[shortest_window[0] : shortest_window[1] + 1]
            if shortest_window is not None
            else ""
        )