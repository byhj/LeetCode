class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        return [sum(nums)-sum(set(nums)),  n*(n+1)/2-sum(set(nums))]