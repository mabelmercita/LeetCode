class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        curr = 0
        maxc = []
        for i in range(len(nums)):
            if nums[i] == 1:
                curr+=1
            if nums[i] == 0:
                maxc.append(curr)
                curr = 0
        maxc.append(curr)
        print(maxc)
        return max(maxc)

           
