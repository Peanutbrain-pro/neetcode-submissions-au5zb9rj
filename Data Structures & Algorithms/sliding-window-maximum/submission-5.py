
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = deque()

        for i in range(k):
            while window and window[-1] < nums[i]:
                window.pop()
            window.append(nums[i])

        output = deque([window[0]])

        for i in range(k, len(nums)):
            if nums[i - k] == window[0]:
                window.popleft()

            while window and window[-1] < nums[i]:
                window.pop()
            window.append(nums[i])

            output.append(window[0])

        return list(output)