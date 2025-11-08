class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        s = 0
        for i in stones:
            if i in jewels:
                s+=1
        return s
        