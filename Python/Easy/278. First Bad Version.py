# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        beg = 1
        end = n
        mid = (beg + end)//2
        while beg <= end:
            if isBadVersion(mid):
                if mid <= 1 or not isBadVersion(mid-1):
                    return mid
                else:
                    end = mid
            else:
                beg = mid+1
            mid = (beg+end)//2
        return mid
        