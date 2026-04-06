class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []
        for i, h in enumerate(heights):
            if not stack:
                stack.append((i, h))
                continue

            top = stack[-1]
            if h > top[1]:
                stack.append((i, h))

            elif h < top[1]:
                prev = None
                while stack:
                    top = stack[-1]
                    if top[1] < h:
                        break
                    max_area = max(top[1] * (i - top[0]), max_area)
                    print("max area: ", max_area)
                    prev = stack.pop()
                if stack:
                    stack.append((prev[0], h))
                else:
                    stack.append((0, h))

        for i, h in stack:
            max_area = max((len(heights) - i) * h, max_area)
            print("max area: ", max_area)

        return max_area
