class Solution(object):
    def sortPeople(self, names, heights):
        return [names[i] for i in sorted(range(len(heights)), key= lambda i: -heights[i])]
        