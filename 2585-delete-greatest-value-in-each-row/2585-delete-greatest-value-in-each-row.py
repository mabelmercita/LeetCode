class Solution(object):
    def deleteGreatestValue(self, grid):
        return sum(map(max,zip(*map(sorted,grid))))
        