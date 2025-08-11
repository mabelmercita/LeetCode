class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range((len(nums)-1),-1,-1):
                if nums[i]+nums[j] == target and i != j:
                    return [i,j]
        