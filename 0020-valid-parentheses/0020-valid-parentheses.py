class Solution(object):
    def isValid(self, s):
        st = []
        t = False
        for i in s:
            if i in '({[':
                st.append(i)
                t = False
            elif st != []:
                if i == ')' and st[-1] == '(':
                    st.pop()
                    t = True
                elif i == '}' and st[-1] == '{':
                    st.pop()
                    t = True
                elif i == ']' and st[-1] == '[':
                    st.pop()
                    t = True
                else:
                    return False
            else:
                return False
        if len(st) > 0 and [']','}',')'] not in st:
            return False
        return t

                
            
            
              

        