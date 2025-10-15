class Solution(object):
    def removeDuplicates(self, nums):
        insertPos = 0
        for num in nums:
            if insertPos < 2 or num != nums[insertPos - 2]:
                nums[insertPos] = num
                insertPos += 1
        return insertPos

        