import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) == h:
            return max(piles)
        minn = 1
        maxx = max(piles)
        max_rate = float('inf')
        while minn <= maxx:
            hours = 0
            rate = (minn+maxx)//2
            for i in piles:
                hours += math.ceil(i/rate)
            if hours <= h:
                max_rate = min(max_rate, rate)
                maxx = rate -1
            else:
                minn = rate + 1
        return max_rate