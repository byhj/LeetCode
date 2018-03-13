class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        ans = 0
        i= 0
        while i < len(nums)-1:
            ans += min(nums[i], nums[i + 1])
            i += 2
        return ans

