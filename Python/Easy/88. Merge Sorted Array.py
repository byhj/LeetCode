class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        end = m + n -1
        end1 = m-1
        end2 = n-1
        while end1 >= 0 and end2 >= 0:
            if nums1[end1] > nums2[end2]:
                nums1[end] = nums1[end1]
                end -= 1
                end1 -= 1
            else:
                nums1[end] = nums2[end2]
                end -= 1
                end2 -= 1
        while end2 >= 0:
            nums1[end] = nums2[end2]
            end -= 1
            end2 -= 1