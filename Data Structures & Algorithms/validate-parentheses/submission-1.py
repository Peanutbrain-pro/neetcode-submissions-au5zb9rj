class Solution:
    def isValid(self, s: str) -> bool:
        rlist = {')' : '(', '}' : '{', ']' : '['}
        llist = ['(', '{', '[']
        stack = []
        
        for char in s:
            if char in llist:
                stack.append(char)
            elif stack and stack[-1] == rlist[char]:
                stack.pop()
            else:
                stack.append(char)
        
        if stack:
            return False
        else:
            return True