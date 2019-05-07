# -*- coding=utf-8 -*-

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) <= 0:
            return True

        stack = []
        mapping = { ")":"(", "}":"{", "]":"[", }

        for char in s:
            if char in mapping:
                top = stack.pop() if len(stack) > 0 else "#"
                if top != mapping[char]:
                    return False
            else:
                stack.append(char)

        return (len(stack) <= 0)

if __name__ == "__main__":
    s = Solution()
    print s.isValid("()")