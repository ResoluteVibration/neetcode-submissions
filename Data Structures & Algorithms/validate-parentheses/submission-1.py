class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        st = []
        par = {')': '(', '}' :'{', ']' : '['}
        for i in s:
            if i in par:
                if not st or st.pop() != par[i]:
                    return False
            else:
                st.append(i)
        return not st