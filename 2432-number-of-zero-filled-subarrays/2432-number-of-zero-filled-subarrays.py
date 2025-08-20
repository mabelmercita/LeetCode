class Solution(object):
    def zeroFilledSubarray(self, nums):
        current_0_subarray = total_0_subarray = 0
        for i in nums:
            if i == 0:
                current_0_subarray += 1
                total_0_subarray += current_0_subarray
            else:
                current_0_subarray = 0
        return total_0_subarray

        