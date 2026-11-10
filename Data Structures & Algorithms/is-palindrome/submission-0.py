class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower().replace(" ", "")
        new = ""
        for i in s:
            if i.isalnum():
                new+=i
        return new == new[::-1]