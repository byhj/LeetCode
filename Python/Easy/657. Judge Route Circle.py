class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        x = y = 0
        for c in moves:
           if c == 'R': x += 1
           elif c == 'L':x -= 1
           elif c == 'U':y += 1
           else: y -= 1
        return x == y == 0
