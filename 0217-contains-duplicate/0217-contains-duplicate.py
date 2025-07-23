class Solution(object):
    def containsDuplicate(self, nums):
        c = set()
        for i in nums:
            if i in c:
                return True
            else:
                c.add(i)
        return False
        
        