class TreeNode:
    def __init__(self, val='0'):
        self.val = val
        self.isEnd = False
        self.children = []

class WordDictionary:

    def __init__(self):
        self.root = TreeNode()

    def addWord(self, word: str) -> None:
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
        if word == '':
            return True

        ptr = self.root
        
        def searchNext(ptr, word):
            if len(word) == 1:
                if word == '.':
                    for child in ptr.children:
                        if child.isEnd:
                            return True
                    return False
                else:
                    for child in ptr.children:
                        if child.val == word and child.isEnd:
                            return True
                    return False

            ch = word[0]
            if ch == '.':
                if any(searchNext(child, word[1:]) for child in ptr.children):
                    return True
                else:
                    return False
            else:
                for child in ptr.children:
                    if child.val == ch:
                        return searchNext(child, word[1:])
                return False

        return searchNext(ptr, word)
            
