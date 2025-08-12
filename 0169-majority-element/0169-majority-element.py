class Solution(object):
    def majorityElement(self, nums):
        max = 0
        maj = 0
        """for i in nums:
            if nums.count(i) > max:
                maj = i
                max = nums.count(i)
        return maj"""

        hash = {}
        for i in nums:
            if i not in hash:
                hash[i] = 1
            else:
                hash[i]+=1
            if hash[i] >max:
                max = hash[i]
                maj = i
        return maj