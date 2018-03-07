class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        beg = move = 0
        end = len(nums)
        while move < end:
            if nums[move] != val:
                nums[beg] = nums[move]
                beg += 1
                move += 1
            else:
                move += 1
        return beg
            
        