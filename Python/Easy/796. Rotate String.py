class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False
        for i in range(len(A)):
            if (A[i:] + A[:i]) == B:
                return True
        return False
    
       # return len(A) == len(B) and B in (A+A)