class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        found = False

        def find_word(i, r, c, visited):
            visited.add((r, c))
            # print(board[r][c], (r, c), visited)
            if word[i] != board[r][c]:
                return False
            elif i == len(word) - 1:
                return True

            for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if nr < 0 or nr >= rows or nc < 0 or nc >= cols or (nr, nc) in visited:
                    continue
                # visited.add((nr, nc))
                if find_word(i+1, nr, nc, visited):
                    return True
                visited.remove((nr, nc))

        rows, cols = len(board), len(board[0])
        for r in range(rows):
            for c in range(cols):
                if find_word(0, r, c, set()):
                    return True
        return False
