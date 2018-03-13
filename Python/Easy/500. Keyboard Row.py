class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        row1 = set('qwertyuiop')
        row2 = set('asdfghjkl')
        row3 = set('zxcvbnm')
        ans = []
        for word in words:
            w = set(word.lower())
            if w & row1 == w or w & row2 == w or w & row3 == w:
                ans.append(word)    # s&t is equal s.intersection(t)
        return ans