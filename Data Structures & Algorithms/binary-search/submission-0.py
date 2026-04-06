class Solution:
    def search(self, nums: List[int], target: int) -> int:
        high = len(nums) - 1
        low = 0
        while True:
            if low > high:
                return -1

            mid = high + low // 2
            if nums[mid] == target:
                return mid
            
            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

            