# -*- coding=utf-8 -*-

def do_init():
    mapping = { 1:"1", }

    now = "1"
    current = 1
    while current < 30:
        result = ""
        char = "#"
        cnt = 0
        for each in now:
            if char == each:
                cnt += 1
            else:
                if cnt:
                    result = "{}{}{}".format(result, cnt, char)
                char = each
                cnt = 1
        if cnt:
            result = "{}{}{}".format(result, cnt, char)
        now = result
        current += 1
        mapping[current] = result
    return mapping

g_mapping = do_init()

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        return g_mapping[n]

if __name__ == "__main__":
    s = Solution()
    for i in xrange(6):
        print s.countAndSay(i+1)
