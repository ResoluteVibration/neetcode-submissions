import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = {
            '+': operator.add,
            '-': operator.sub,
            '/': operator.truediv,
            '*': operator.mul
        }
        st = []
        for i in tokens:
            if i.isnumeric():
                st.append(int(i))
            elif i not in '+-*/':
                st.append(int(i))
            elif i in operations:
                b = st.pop()
                a = st.pop()
                st.append(int(operations[i](a,b)))
        return st[-1]