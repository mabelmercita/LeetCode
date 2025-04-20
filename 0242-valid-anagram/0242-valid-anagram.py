class Solution(object):
    def isAnagram(self, s, t):
        l1 = list(s)
        l1.sort()
        l2 = list(t)
        l2.sort()
        '''print(l1)
        print(l2)'''
        if l1 == l2:
            return True
        else:
            return False
