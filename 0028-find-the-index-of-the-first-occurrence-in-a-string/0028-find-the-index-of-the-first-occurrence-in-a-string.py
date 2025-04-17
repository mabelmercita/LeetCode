class Solution(object):
    def strStr(self, haystack, needle):
        if needle not in haystack:
            return -1
        elif needle == haystack:
            return 0
        else:
            d = {}
            for i in range(len(haystack)):
                l=[]
                for j in range(i,len(haystack)+1):
                    l.append(haystack[i:j])
                d[i] = l
                l = []
            for i in d:
                #if i == len(haystack)-1:
                for j in d[i]:

                    if j == needle:
                        return i
            
    
        