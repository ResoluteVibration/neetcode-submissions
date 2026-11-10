import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower().translate(str.maketrans("",""," "+string.punctuation))
        return s == s[::-1]