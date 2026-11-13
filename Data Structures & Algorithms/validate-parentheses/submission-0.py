class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        if n == 0 or n % 2 != 0:
            return False
        st = []
        par = {'(': ')', '{' :'}', '[' : ']'}
        for i in s:
            if i in par.keys():
                st.append(i)
            if i in par.values():
                if len(st) > 0 and i == par[st[-1]]:
                    st.pop()
                else:
                    return False
        return not st