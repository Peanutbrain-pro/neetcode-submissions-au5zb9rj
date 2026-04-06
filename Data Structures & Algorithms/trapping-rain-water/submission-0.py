class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 1:
            return 0

        maxLeft = []
        t = 0
        for h in height:
            maxLeft.append(t)
            if h > t:
                t = h

        maxRight = []
        t = 0
        for h in height[::-1]:
            maxRight.insert(0, t)
            if h > t:
                t = h

        water = 0
        for i in range(len(maxLeft)):
            temp = min(maxLeft[i], maxRight[i]) - height[i]
            if temp > 0:
                water += temp

        return water