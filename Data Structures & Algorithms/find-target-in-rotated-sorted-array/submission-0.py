class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        h = len(nums) - 1

        while h >= l:
            mid = l + (h - l) // 2
            mid_num = nums[mid]

            if mid_num == target:
                return mid

            if nums[l] <= mid_num:
                # left half is sorted
                if target >= nums[l] and target <= mid_num:
                    h = mid - 1
                else:
                    l = mid + 1
            else:
                # right half is sorted
                if target >= mid_num and target <= nums[h]:
                    l = mid + 1
                else:
                    h = mid - 1

        return -1