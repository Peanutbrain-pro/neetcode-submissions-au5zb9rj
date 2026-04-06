
class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)
        if length <= 1:
            return 0

        maxLeft = [0]*length
        t = 0
        for i, h in enumerate(height):
            maxLeft[i] = t
            if h > t:
                t = h

        maxRight = [0]*length
        t = 0
        for i, h in enumerate(height[::-1]):
            maxRight[length - i - 1] = t
            if h > t:
                t = h

        water = 0
        for i in range(len(maxLeft)):
            temp = min(maxLeft[i], maxRight[i]) - height[i]
            if temp > 0:
                water += temp

        return water