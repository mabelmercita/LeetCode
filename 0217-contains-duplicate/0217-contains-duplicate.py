class Solution(object):
    def containsDuplicate(self, nums):
        nset = set()
        for i in nums:
            if i in nset:
                return True
            nset.add(i)
        return False
            

        