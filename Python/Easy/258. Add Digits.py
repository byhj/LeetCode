class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num >= 10:
            n = num
            num = 0
            while n != 0:
                num += n % 10
                n //= 10
        return num
