class Solution(object):
    def plusOne(self, digits):
        l = []
        str1 = ''
        for i in digits:
            str1 = str1+str(i)
        for i in str(int(str1)+1):
            l.append(int(i))
        return l

        