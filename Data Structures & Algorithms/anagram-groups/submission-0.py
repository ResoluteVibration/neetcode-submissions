class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lst = {}
        for i in strs:
            key = "".join(sorted(i))
            if key not in lst:
                lst[key] = []
            lst[key].append(i)
        return list(lst.values())
