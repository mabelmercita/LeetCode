class Solution(object):
    def isAcronym(self, words, s):
        a = ''
        for i in range(len(words)):
            a += words[i][0]
        if a == s:
            return True
        else:
            return False        
        