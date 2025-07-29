class Solution(object):
    def findDuplicate(self, nums):
        nset = set()
        for i in nums:
            if i in nset:
                return i
            else:
                nset.add(i)
                
        