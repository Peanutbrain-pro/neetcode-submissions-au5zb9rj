class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        item_checked = 0
        i = 0
        while (item_checked < len(nums)):
            if nums[i] == 0:
                nums.insert(0, nums.pop(i))
                i += 1
                item_checked += 1
            elif nums[i] == 2:
                nums.append(nums.pop(i))
                item_checked += 1
            else:
                i += 1
                item_checked += 1