class Solution(object):
    def plusOne(self, digits):
        l = []
        str1 = ''
        for i in digits:
            str1 = str1+str(i)
        s = int(str1)+1
        str2 = str(s)
        for i in str2:
            l.append(int(i))
        return l

        