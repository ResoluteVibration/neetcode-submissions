class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:    
        dl = [0]*len(temperatures) 
        st = []
        for i in range(len(temperatures)):
            while st and temperatures[i] > temperatures[st[-1]]:
                prev = st.pop()
                dl[prev] = i-prev
            st.append(i)
        return dl