class Solution(object):
    def insert(self, nums1, max, idx1, val):
        idx = max
        while idx > idx1:
            nums1[idx] = nums1[idx - 1]
            idx -= 1
        nums1[idx1] = val

    def merge(self, nums1, m, nums2, n):
        idx1 = 0
        idx2 = 0
        cnt = 0
        while idx1 < m + cnt and idx2 < n:
            if nums1[idx1] <= nums2[idx2]:
                idx1 += 1
            else:
                self.insert(nums1, m + cnt, idx1, nums2[idx2])
                cnt += 1
                idx1 += 1
                idx2 += 1
        while idx2 < n:
            nums1[m + cnt] = nums2[idx2]
            idx2 += 1
            cnt += 1
        
        return nums1


if __name__ == "__main__":
    s = Solution()
    print s.merge([4,0,0,0,0,0],1,[1,2,3,5,6],5)