class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        max_area = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != 1:
                    continue

                area = 0
                # Flatten coordinates into a single integer (r * cols + c)
                # to avoid allocating (r, c) tuples
                stack = [r * cols + c]
                grid[r][c] = 0

                while stack:
                    curr = stack.pop()
                    cr = curr // cols
                    cc = curr % cols
                    area += 1

                    # Unrolled directional checks (no 'for' loop over directions)
                    if cr > 0 and grid[cr - 1][cc]:
                        grid[cr - 1][cc] = 0
                        stack.append((cr - 1) * cols + cc)
                    if cr + 1 < rows and grid[cr + 1][cc]:
                        grid[cr + 1][cc] = 0
                        stack.append((cr + 1) * cols + cc)
                    if cc > 0 and grid[cr][cc - 1]:
                        grid[cr][cc - 1] = 0
                        stack.append(cr * cols + (cc - 1))
                    if cc + 1 < cols and grid[cr][cc + 1]:
                        grid[cr][cc + 1] = 0
                        stack.append(cr * cols + (cc + 1))

                if area > max_area:
                    max_area = area

        return max_area