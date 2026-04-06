class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        nums.sort()
        result = []

        for i, num in enumerate(nums):
            if i > 0 and num == nums[i - 1]:
                continue

            left, right = i + 1, length - 1
            while left < right:
                total = nums[left] + nums[right] + num
                if total == 0:
                    trio = [num, nums[left], nums[right]]
                    # if trio not in result:
                    result.append(trio)
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                    # right -= 1
                    # while nums[right] == nums[right + 1] and right > left:
                    #     right -= 1
                elif total < 0:
                    left += 1
                    # while nums[left] == nums[left - 1] and left < right:
                    #     left += 1
                else:
                    right -= 1
                    # while nums[right] == nums[right + 1] and right > left:
                    #     right -= 1

        return result