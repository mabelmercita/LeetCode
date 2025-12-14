class Solution(object):
    def shuffle(self, nums, n):
        l1 = nums[0:n]
        l2 = nums[n:len(nums)]
        l3 = []
        j = k = 0
        for i in range(len(nums)):
            if i%2 == 0:
                l3.append(l1[j])
                j+=1
            else:
                l3.append(l2[k])
                k+=1
        return l3
        