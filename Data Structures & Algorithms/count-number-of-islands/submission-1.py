class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "0":
                    continue
                # print("found 1 at ", r, c, ": ", grid[r][c])

                count += 1
                # Perform dfs search and make them all 0
                # visited = set()
                stack = [(r, c)]
                grid[r][c] = 0
                while stack:
                    (x, y) = stack.pop()
                    # visited.add((x, y))
                    for (dr, dc) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nr = x + dr
                        nc = y + dc
                        if nc < 0 or nc >= cols or nr < 0 or nr >= rows:
                            continue

                        if grid[nr][nc] == "1":
                            grid[nr][nc] = "0"
                            stack.append((nr, nc))
                
                # for row in grid:
                #     print(row)
                # print("\n")

        return count
                