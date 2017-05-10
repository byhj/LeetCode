class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        for val in nums:
            sum ^= val
        return sum
        