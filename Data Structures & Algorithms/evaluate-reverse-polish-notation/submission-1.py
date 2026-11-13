class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for i in tokens:
            if i.isnumeric():
                st.append(int(i))
            elif i not in '+-*/':
                st.append(int(i))
            elif i in '+-*/':
                b = st.pop()
                if i == '/' and b == 0 :
                    return 0
                a = st.pop()
                match i:
                    case '+':
                        st.append(a+b)
                    case '-':
                        st.append(a-b)
                    case '*':
                        st.append(a*b)
                    case '/':
                        st.append(int(a/b))
        return st[-1]