class Solution(object):
    def addDigits(self, num):
        s = num
        while num >= 10:
            
            s=0
            while num != 0:
                s += num%10
                num= num//10
            num = s
        return s
        