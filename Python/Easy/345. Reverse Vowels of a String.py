class Solution:

    def isVowels(self, c):
        c = c.lower()
        return c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u'

    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        sl = list(s)
        beg = 0
        end = len(sl) - 1
        while beg < end:
            if self.isVowels(sl[beg]) and self.isVowels(sl[end]):
                sl[beg], sl[end] = sl[end], sl[beg]
                beg += 1
                end -= 1
            elif not self.isVowels(sl[beg]):
                beg += 1
            elif not self.isVowels(sl[end]):
                end -= 1
        return ''.join(sl)
