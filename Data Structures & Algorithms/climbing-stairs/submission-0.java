class Solution {
    public int climbStairs(int n) {
        int a = 1, b = 2, c = 2;
        if (n == 1 || n == 2) {
            return n;
        }
        while (c < n) {
            int temp = b;
            b = b + a;
            a = temp;
            c++;
        }

        return b;
    }
}
