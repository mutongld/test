class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        size = len(nums)
        idx = 0
        while idx < size:
            if nums[idx] == val:
                nums[idx] = nums[size - 1]
                size -= 1
            else:
                idx += 1
        return size

if __name__ == "__main__":
    s = Solution()
    l = [1,2,3,4,5,6,4,3,2,1]
    print s.removeElement(l, 3)
    print l