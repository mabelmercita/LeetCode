class Solution(object):
    def isSameAfterReversals(self, num):
        snum = str(num)
        rev1 = snum[::-1]
        rev1num = int(rev1)
        snum2 = str(rev1num)
        rev2 = snum2[::-1]
        rev2num = int(rev2)
        if num == rev2num:
            return True
        else:
            return False
        