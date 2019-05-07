# -*- coding=utf-8 -*-

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        cnt = 1
        last_idx = idx = 0
        last = nums[idx]
        limit = len(nums)
        while idx < limit:
            if nums[idx] != last:
                if last_idx != idx:
                    nums[last_idx + 1] = nums[idx]
                    last_idx += 1
                last = nums[idx]
                cnt += 1

            idx += 1
        return cnt

if __name__ == "__main__":
    s = Solution()
    print s.removeDuplicates([0,0,1,1,1,2,2,3,3,4])
