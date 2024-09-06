class Solution(object):  
    def getLongestSubsequence(self, words, groups):  
        longest_subsequence = []  
        
        # Starting with the first word
        longest_subsequence.append(words[0])
        last_group = groups[0]
        
        for i in range(1, len(words)):
            # If the group differs from the last added, we can add this word
            if groups[i] != last_group:
                longest_subsequence.append(words[i])
                last_group = groups[i]
        
        return longest_subsequence
