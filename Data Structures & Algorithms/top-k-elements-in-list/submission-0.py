class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        lst = defaultdict(int)
        for i in nums:
            lst[i] += 1
        srt_lst = sorted(lst, key = lambda x: lst[x], reverse = True)
        return srt_lst[:k]