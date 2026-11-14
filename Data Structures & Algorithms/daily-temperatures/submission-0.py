class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)      
        dl = [0]*n
        st = []
        for i in range(n):
            while st and temperatures[i] > temperatures[st[-1]]:
                prev = st.pop()
                dl[prev] = i-prev
            st.append(i)
        return dl