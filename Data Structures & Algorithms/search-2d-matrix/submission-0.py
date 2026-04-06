class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # find row in log(m) and then find the column in log(n)
        m, n = len(matrix) - 1, len(matrix[0]) - 1
        low, high = 0, m
        select_row = 0
        while True:
            if low > high:
                return False

            mid = (low + high) // 2
            if matrix[mid][0] <= target and matrix[mid][n] >= target:
                select_row = mid
                break
            elif matrix[mid][0] > target:
                high = mid - 1
            else:
                low = mid + 1

        low, high = 0, n
        while True:
            if low > high:
                return False
            
            mid = (low + high) // 2
            if matrix[select_row][mid] == target:
                return True
            elif matrix[select_row][mid] < target:
                low = mid + 1
            else:
                high = mid - 1
            
        
