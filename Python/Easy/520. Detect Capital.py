class Solution:
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        n = 0
        for c in word:
            if c.isupper():
                n += 1
        return n == len(word) or n == 0 or n==1 and word[0].isupper()
        