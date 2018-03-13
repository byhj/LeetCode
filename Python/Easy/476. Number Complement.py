class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        #flip  one bit each time
        i = 1
        while num >= i:
            num ^= i;
            i <<= 1
        return num
        