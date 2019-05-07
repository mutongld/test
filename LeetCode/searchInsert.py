# -*- coding=utf-8 -*-

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0
        
        for idx, val in enumerate(nums):
            if val >= target:
                return idx
        
        return len(nums)

if __name__ == "__main__":
    s = Solution()
    print s.searchInsert([1,3,5,6], 0)
