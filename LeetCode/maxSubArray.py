# -*- coding=utf-8 -*-

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 0:
            return 0

        now_sum = 0
        max_sum = 0
        init = 0

        for val in nums:
            now_sum += val
            if now_sum > max_sum or init == 0:
                max_sum = now_sum
                init = 1
            if now_sum < 0:
                now_sum = 0

        return max_sum

if __name__ == "__main__":
    s = Solution()
    print s.maxSubArray([-3,-2,0,])