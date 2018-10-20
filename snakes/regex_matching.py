#This one: https://leetcode.com/problems/regular-expression-matching/description/
from enum import Enum

class States(Enum):
    waiting = 0
    gotTemplate = 1
    matchAll = 2

class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        return not ""


print(Solution().isMatch("a", "ab*.*....ass"))






