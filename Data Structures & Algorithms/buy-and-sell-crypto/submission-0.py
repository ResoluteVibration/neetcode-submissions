class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mp = float('inf')        
        maxp = 0
        for i in prices:
            mp = min(mp,i)
            p = i-mp
            maxp = max(p,maxp)
        return maxp