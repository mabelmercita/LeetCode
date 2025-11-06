class Solution(object):
    def mostWordsFound(self, sentences):
        max = 0
        for i in sentences:
            l = i.split()
            if len(l)>max:
                max = len(l)
        return max
        