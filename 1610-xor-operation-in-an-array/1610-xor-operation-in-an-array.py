class Solution(object):
    def xorOperation(self, n, start):
        ans = 0
        nums = [start + n * 2 for n in range(n)]
        
        for n in nums:
            ans = ans ^ n
        return ans 
        