class Solution(object):
    def isPowerOfFour(self, n):
        if n == 1:
            return True
        elif n <= 0:
            return False
        log_base4 = math.log(n)/math.log(4)
        return (log_base4 == int(log_base4))
        