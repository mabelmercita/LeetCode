class Solution(object):
    def countPrefixSuffixPairs(self, words):
       c = 0
       def isPrefixAndSuffix(str1, str2):
            '''if len(str2)/2 == 0:
                half_len = len(str2)/2
            else:
                half_len = int((len(str2)/2)) + 1'''
            '''if str1 in str2[:half_len] and str1 in str2[half_len:0:-1]:'''
            if str2.startswith(str1) and str2.endswith(str1):
                return True
            else:
                return False
       for i in range(len(words)):
            str1 = words[i]
            for j in range(i+1,len(words)):
                    str2 = words[j] 
                    if isPrefixAndSuffix(str1, str2):
                        c += 1
       return c

         


        