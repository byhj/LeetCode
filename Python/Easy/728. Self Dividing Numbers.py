class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        ans = []
        for num in range(left, right+1):
            flag = 1
            a = num
            while a != 0:
                c = a % 10
                if c == 0 or num % c != 0:
                    flag = 0
                    break
                a /= 10
                a = int(a)
            if flag == 1:
                ans.append(num)
        return ans
            
          