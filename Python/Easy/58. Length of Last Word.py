class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        sl = s.split()
        return 0 if not sl else len(sl[len(sl)-1])