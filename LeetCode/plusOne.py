# -*- coding=utf-8 -*-

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        idx = len(digits) - 1
        while idx >= 0:
            num = digits[idx] + 1
            digits[idx] = num % 10
            num = num / 10
            if num <= 0:
                break
            idx -= 1
        
        if num > 0:
            digits = [num] + digits
        
        return digits

if __name__ == "__main__":
    s = Solution()
    print s.plusOne([9,9])