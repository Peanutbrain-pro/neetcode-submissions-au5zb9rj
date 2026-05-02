class TreeNode:
    def __init__(self, val=None):
        # self.val = val
        self.isEnd = False
        self.children = {}

    def addWord(self, word):
        ptr = self
        for char in word:
            if char not in ptr.children:
                ptr.children[char] = TreeNode()
            ptr = ptr.children[char]
        ptr.isEnd = True

    def removeLastSingleNodes(self, word):
        ptr = self
        path = []
        for char in word:
            path.append((char, ptr))
            ptr = ptr.children[char]

        for c, parent in reversed(path):
            if not len(parent.children) or c not in parent.children:
                del parent.children[c]
            else:
                return


class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        root = TreeNode()

        # First create trie of th words
        for word in words:
            root.addWord(word)

        rows, cols = len(board), len(board[0])

        result = set()
        visited = set()

        def dfs(x, y, word, node):
            if (
                x < 0
                or y < 0
                or x >= cols
                or y >= rows
                or (x, y) in visited
                or board[y][x] not in node.children
            ):
                return

            # print((x, y), "word: ", word)
            word += board[y][x]
            # print(word)

            visited.add((x, y))
            child = node.children[word[-1]]
            if child.isEnd:
                child.isEnd = False
                root.removeLastSingleNodes(word)
                result.add(word)

            dfs(x - 1, y, word, child)
            dfs(x + 1, y, word, child)
            dfs(x, y - 1, word, child)
            dfs(x, y + 1, word, child)

            visited.remove((x, y))

        # Now for every single position in the board, find words from the Trie
        for x in range(cols):
            for y in range(rows):
                dfs(x, y, "", root)

        return list(result)
