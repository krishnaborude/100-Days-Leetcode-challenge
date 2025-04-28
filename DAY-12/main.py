class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i = 0
        for char in t:
            if i < len(s) and s[i] == char:
                i += 1
        return i == len(s)
