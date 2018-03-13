class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join(s.split()[::-1])[::-1]
        # first reverse the order of the words and then reverse the entire string.
        # return ' '.join(x[::-1] for x in s.split())
        
        