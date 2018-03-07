class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        beg = 0
        move = 0
        while move < n:
            if nums[move] != 0 :
                nums[beg] = nums[move]
                beg += 1
                move += 1
            else:
                move += 1
        for i in range(beg, n):
            nums[i] = 0