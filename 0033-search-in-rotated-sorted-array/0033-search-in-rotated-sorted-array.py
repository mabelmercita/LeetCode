class Solution(object):
    def search(self, nums, target):
        c = 0
        for i in range(len(nums)):
            if nums[i] == target:
                return i
                c += 1
        else:
            if c == 0:
                return -1
        