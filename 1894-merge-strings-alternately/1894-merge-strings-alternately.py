class Solution(object):
    def mergeAlternately(self, word1, word2):
        
        new = ''
        gl = word1 if len(word1) > len(word2) else word2
        sw =  word2 if len(word2) < len(word1) else word1

        for i in range(len(gl)):
            if i < len(sw):
                new += word1[i]+word2[i]
            else:
                new+=gl[i]
        return new

        