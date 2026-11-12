class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_len = 0
        max_freq = 0
        seen = {}
        for right in range(len(s)):
            r = s[right]
            seen[r] = seen.get(r, 0)+ 1
            while (right - left + 1) - max(seen.values()) > k:
                seen[s[left]] -= 1
                left += 1
            length = right - left + 1
            max_len = max(max_len, length)
        return max_len