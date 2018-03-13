class Solution:
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        #There are len(set(candies)) unique candies, and the sister picks only          len(candies) / 2 of them, so she can¡¯t have more than this amount.
        return min(len(candies)//2, len(set(candies)))