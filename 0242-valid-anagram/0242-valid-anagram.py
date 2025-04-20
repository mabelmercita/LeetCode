class Solution(object):
    def isAnagram(self, s, t):
        '''l1 = list(s)
        l1.sort()
        l2 = list(t)
        l2.sort()'''
        '''print(l1)
        print(l2)'''
        if sorted(list(s)) == sorted(list(t)):
            return True
        else:
            return False
