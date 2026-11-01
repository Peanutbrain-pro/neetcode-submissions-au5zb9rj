class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # use BFS from each position of the gate simultaneously 

        rows = len(grid)
        cols = len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        # visited = set()
        # list of queues
        queues = []

        def bfs_increment(r, c, queue_index):
            curr_val = grid[r][c]
            for (dr, dc) in directions:
                nr, nc = r+dr, c+dc
                if nr < 0 or nr >= rows \
                   or nc < 0 or nc >= cols \
                   or grid[nr][nc] != 2147483647:
                   continue
        
                grid[nr][nc] = curr_val + 1
                queues[queue_index].append((nr, nc))
                # visited.add((nr, nc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queues.append([(r, c)])

        while any(queues):
            for i in range(len(queues)):
                if not queues[i]:
                    continue
            
                queue_length = len(queues[i])
                for _ in range(queue_length):
                    r, c = queues[i].pop(0)
                    bfs_increment(r, c, i)

            # for row in grid:
            #     print(row)
            # print()

