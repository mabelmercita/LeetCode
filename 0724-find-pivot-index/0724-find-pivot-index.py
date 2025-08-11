class Solution(object):
    def pivotIndex(self, nums):
        left = 0
        right = sum(nums)

        for i in range(len(nums)):
            right -= nums[i]
            if left == right:
                return i
            left+=nums[i]
        return -1