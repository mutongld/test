# -*- coding=utf-8 -*-

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if haystack == needle or needle == "":
            return 0

        if not haystack or not needle:
            return -1
        
        len1 = len(haystack)
        len2 = len(needle)
        if len1 < len2:
            return -1

        for i in xrange(len1 - len2 + 1):
            if haystack[i:i+len2] == needle:
                return i

        return -1

if __name__ == "__main__":
    s = Solution()
    print s.strStr(haystack = "a", needle = "")
