class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dict = {}
        ans = []
        for n in nums1:
            if n not in dict:
               dict[n] = 1
            else:
               dict[n] += 1

        for n in nums2:
             if n in dict and (dict[n] - 1) >= 0:
                 ans.append(n)
                 dict[n] -= 1
        return ans