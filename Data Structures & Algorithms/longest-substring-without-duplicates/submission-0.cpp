class Solution {
public:
int lengthOfLongestSubstring(string s) {
    int start = 0, end = 0, longest = 0, length;

    if (s[0] == '\0') return 0;
    if (s[1] == '\0') return 1;

    for (int i = 1; s[i] != '\0'; i++) {
        length = end - start + 1;
        if (length > longest) longest = length;

        // s[i] is the latest found char, checking if duplicate exists
        for (int d = start; d <= end; d++) {
            // If duplicate exists
            if (s[i] == s[d]) {
                // moving start to after the found duplicate
                start = d + 1;
                
                // end value only changes when end == d
                if (end == d) end += 1;

                break;
            }
        }

        if (end != i) end++;
    }
    
    length = end - start + 1;
    if (length > longest) longest = length;

    return longest;

}
};
