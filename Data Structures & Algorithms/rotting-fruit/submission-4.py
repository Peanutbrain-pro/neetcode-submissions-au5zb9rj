class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        # list of queues of (r, c)
        queues = []
        minutes = 0

        def bfs_rot(r, c, queue_index):
            rotted = False
            for (dr, dc) in directions:
                nr = r + dr
                nc = c + dc

                if nr < 0 or nr >= rows or nc < 0 or nc >= cols \
                    or grid[nr][nc] != 1:
                    continue

                grid[nr][nc] = 2
                queues[queue_index].append((nr, nc))
                rotted = True
            # if not rotted: print("no more rotten fruits")
            return rotted


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queues.append([(r, c)])

        while any(queues):
            # print("minutes: ", minutes)
            number_of_rotted = 0
            for i in range(len(queues)):
                if not queues[i]:
                    continue
                
                queue_length = len(queues[i])
                for y in range(queue_length):
                    r, c = queues[i].pop(0)
                    number_of_rotted += bfs_rot(r, c, i)
                    

            if number_of_rotted:
                minutes += 1

            # print("minutes: ", minutes)
            # print("queues: ", queues)
            # for row in grid:
            #     print(row)
            # print()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1

        return minutes