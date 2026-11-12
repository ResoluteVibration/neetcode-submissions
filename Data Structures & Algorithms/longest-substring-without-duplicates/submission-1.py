class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_len = 0
        seen = {}
        for right in range(len(s)):
            r = s[right]
            if r in seen and seen[r] >= left:
                left = seen[r] + 1
            seen[r] = right
            l = right - left + 1
            max_len = max(max_len, l)
        return max_len