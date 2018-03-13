class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic1 = {}
        dic2 = {}
        for ch in s:
            dic1[ch] = dic1.get(ch, 0) + 1
        for ch in t:
            dic2[ch] = dic2.get(ch, 0) + 1
        return dic1 == dic2

#   return sorted(s) == sorted(t)