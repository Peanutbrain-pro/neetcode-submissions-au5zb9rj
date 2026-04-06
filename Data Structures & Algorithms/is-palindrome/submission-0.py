class Solution:
    def isPalindrome(self, s: str) -> bool:
        stringlist = [char.lower() for char in list(s) if char.isalnum()]
        if stringlist[::-1] == stringlist:
            return True
        return False