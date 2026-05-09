class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [[0 for _ in range(n)] for _ in range(n)]
        # number represents number of marks, queens can be placed at 0
        # only store the vertical and diagonal down marks from queen position
        # store -1 in places of Queen

        result = []

        def dfs(row):
            # print(row, board)
            if row == n:
                # print("Found one", result)
                result.append(["".join(["Q" if c == -1 else "." for c in row]) for row in board])
                return
            
            for c in range(n):
                # print("iterating over ", board[row])
                if board[row][c] > 0:
                    continue

                board[row][c] = -1
                # print("Queen position selected: ", c, "in row:", row)
                # print(board)

                # mark all vertical and diagonal down
                for r in range(row+1, n):
                    disp = r - row
                    board[r][c] += 1

                    if c - disp >= 0:
                        board[r][c - disp] += 1
                    if c + disp < n:
                        board[r][c + disp] += 1

                dfs(row+1)

                # unmark all below
                for r in range(row+1, n):
                    disp = r - row
                    board[r][c] -= 1
                    if c - disp >= 0:
                        board[r][c - disp] -= 1
                    if c + disp < n:
                        board[r][c + disp] -= 1
                board[row][c] = 0

        dfs(0)
        return result