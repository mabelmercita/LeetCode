class Solution(object):
    def maxRepeating(self, sequence, word):
        n = len(sequence)
        c = 0
        k = 1
        for i in range(n):
            if word*k in sequence:
                c += 1
                k += 1
            if k > n:
                break
        return c
        
        