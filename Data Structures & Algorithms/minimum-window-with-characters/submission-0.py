from collections import Counter as count
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        left = 0
        have = 0
        res = ""
        window = {}
        required = count(t)
        need = len(required)        
        min_len = float("inf")
        for right in range(len(s)):
            r = s[right]
            window[r] = window.get(r,0) + 1
            if r in required and window[r] == required[r]:
                have += 1
            while have == need:
                l = right - left + 1
                if l < min_len:
                    min_len = l
                    res = s[left : right + 1]
                l = s[left]
                window[l] -= 1
                if l in required and window[l] < required[l]:
                    have -= 1
                left += 1
        return res