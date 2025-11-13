class Solution(object):
    def selfDividingNumbers(self, left, right):
        res = []
        for i in range(left, right + 1):
            s = str(i)
            for ch in s:
                digit = int(ch)
                if digit == 0 or i % digit != 0:
                    break
            else:
                res.append(i)
        return res