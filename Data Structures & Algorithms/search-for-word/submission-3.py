class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        found = False

        def find_word(i, r, c):
            # visited.add((r, c))

            # print(board[r][c], (r, c), visited)
            if word[i] != board[r][c]:
                return False
            elif i == len(word) - 1:
                return True

            temp = board[r][c]
            board[r][c] = '#'
            for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if nr < 0 or nr >= rows or nc < 0 or nc >= cols or board[nr][nc] == "#":
                    continue
                # visited.add((nr, nc))
                if find_word(i+1, nr, nc):
                    return True
                # visited.remove((nr, nc))

            board[r][c] = temp

        w_freq = {}
        for char in word:
            w_freq[char] = w_freq.get(char, 0) + 1

        # If there aren't enough letters for each character in the matrix, then no point in searching
        rows, cols = len(board), len(board[0])
        for r in range(rows):
            for c in range(cols):
                if board[r][c] in w_freq:
                    w_freq[board[r][c]] -= 1
        for key in w_freq:
            if w_freq[key] > 0:
                return False

        for r in range(rows):
            for c in range(cols):
                if find_word(0, r, c):
                    return True
        return False
