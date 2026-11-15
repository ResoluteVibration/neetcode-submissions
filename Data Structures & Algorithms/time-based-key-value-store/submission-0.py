class TimeMap:

    def __init__(self):
        self.dictHash = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dictHash:
            self.dictHash[key] = []
        self.dictHash[key].append((value, timestamp))  

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dictHash:
            return ""
        arr = self.dictHash[key]
        left = 0
        right = len(arr) - 1
        res = ''
        while left <= right:
            mid = (left+right)//2
            if arr[mid][1] <= timestamp:
                res = arr[mid][0]
                left = mid + 1
            else:
                right = mid - 1
        return res       
