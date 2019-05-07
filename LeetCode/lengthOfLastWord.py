# -*- coding=utf-8 -*-

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        idx = len(s) - 1
        size = 0
        while idx >= 0:
            if s[idx] != ' ':
                size += 1
            elif size > 0:
                return size
            idx -= 1
        return size

if __name__ == "__main__":
    s = Solution()
    print s.lengthOfLastWord("hello")
