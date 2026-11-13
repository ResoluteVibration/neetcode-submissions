from collections import Counter as count
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        if n > len(s2):
            return False
        s1_count = count(s1)
        window = count(s2[:n])
        if window == s1_count:
            return True
        for i in range(n,len(s2)):
            window[s2[i]] += 1
            left_char = s2[i-n]
            window[left_char] -= 1
            if window[left_char] == 0:
                del window[left_char]
            if window == s1_count:
                return True
        return False