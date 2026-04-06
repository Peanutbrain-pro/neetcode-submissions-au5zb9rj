class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Duplicate for each row
        for row in board:
            row_set = set()
            for r in row:
                if r in row_set:
                    return False
                if r != ".":
                    row_set.add(r)

        # Duplicate for each column
        for i in range(9):
            col_set = set()
            for j in range(9):
                item = board[j][i]
                if item in col_set:
                    return False
                if item != ".":
                    col_set.add(item)

        # Duplicate for each 3x3 grid
        for i in range(3):
            for j in range(3):
                # i*3, j*3 gives the starting pos of each 3x3 grid
                # I need to get (i, j), (i, j+1), (i, j+2), (i+1, j), (i+1, j+1), etc.
                grid_hash = set()
                for x in range(3):
                    for y in range(3):
                        item = board[i * 3 + x][j * 3 + y]
                        if item in grid_hash:
                            return False
                        if item != ".":
                            grid_hash.add(item)
        return True

