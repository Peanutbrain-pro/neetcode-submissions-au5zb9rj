class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        rows = len(grid)
        cols = len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    continue

                area = 1
                grid[r][c] = 0
                stack = [(r, c)]
                while stack:
                    x, y = stack.pop()
                    for dx, dy in directions:
                        nr, nc = x + dx, y + dy
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc]:
                            area += 1
                            grid[nr][nc] = 0
                            stack.append((nr, nc))

                maxArea = max(area, maxArea)
        return maxArea