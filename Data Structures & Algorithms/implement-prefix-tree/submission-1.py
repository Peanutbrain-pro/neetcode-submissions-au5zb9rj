class TreeNode:
    def __init__(self, val = '0'):
        self.val = val
        self.isEnd = False
        self.children = []

class PrefixTree:

    def __init__(self):
        self.root = TreeNode()

    def insert(self, word: str) -> None:
        if word == '':
            return

        ptr = self.root
        for char in word:
            child = None
            for ch in ptr.children:
                if ch.val == char:
                    child = ch
                    break
            if not child:
                temp = TreeNode(char)
                ptr.children.append(temp)
                ptr = temp
            else:
                ptr = child

        if ptr != self.root:
            ptr.isEnd = True

    def search(self, word: str) -> bool:
        ptr = self.root
        for char in word:
            found = False
            child = None
            for ch in ptr.children:
                if ch.val == char:
                    found = True
                    child = ch
                    break
            if not found:
                return False
            ptr = child

        if ptr != self.root and ptr.isEnd == True:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        ptr = self.root
        for char in prefix:
            found = False
            child = None
            for ch in ptr.children:
                if ch.val == char:
                    found = True
                    child = ch
                    break
            if not found:
                return False
            ptr = child

        if ptr != self.root:
            return True
        else:
            return False
        
        