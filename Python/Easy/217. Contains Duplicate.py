class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dic = {}
        for n in nums:
            dic[n] = dic.get(n, 0) + 1
            if dic[n] > 1:
                return True
        return False

# return len(nums) > len(set(nums))