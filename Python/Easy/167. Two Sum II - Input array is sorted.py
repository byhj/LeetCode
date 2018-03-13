class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(numbers)
        ans = []
        for i in range(n-1):
            #binary search for target - numbers[i]
            t = target-numbers[i]
            beg = i+1
            end = n-1
            mid = (beg+end) // 2
            while beg <= end:
                if numbers[mid] == t:
                    ans.append(i+1)
                    ans.append(mid+1)
                    return ans
                elif numbers[mid] > t:
                    end = mid-1
                else:
                    beg = mid+1
                mid = (beg+end) // 2
        return ans
 

```
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(numbers)
        ans = []
        beg = 0
        end = n-1
        while beg < end:
            a = numbers[beg]
            b = numbers[end]
            if a + b == target:
                ans.append(beg+1)
                ans.append(end+1)
                break
            elif a + b > target:
                end -= 1
            else:
                beg += 1
        return ans
```      