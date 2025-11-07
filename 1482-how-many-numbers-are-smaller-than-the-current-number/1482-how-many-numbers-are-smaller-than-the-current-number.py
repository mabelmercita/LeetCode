class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        l = []
        for i in nums:
            minc = 0
            for j in nums:
                if j<i:
                    minc += 1
            l.append(minc)
        return l
        