# This problem: https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int

        The approach is like this
        - two pointers mark beginning and end of substring
        - move string tail until find repeat
        - document substring length
        """

        if len(s) == 1 or len(s) == 0:
            return len(s)
        hashedString = {}
        longestSize = 1
        head = 0
        tail = 1
        while s[head] == s[tail]:
            head += 1
            tail += 1
            if tail >= len(s):
                return longestSize
        longestSize = 2

        hashedString[s[head]] = head
        hashedString[s[tail]] = tail

        while tail < len(s) - 1:
            tail += 1
            if s[tail] in hashedString:
                if len(hashedString) > longestSize:
                    longestSize = len(hashedString)
                oldHead = head
                head = hashedString[s[tail]] + 1
                for i in range(oldHead, head):
                    del hashedString[s[i]]
            hashedString[s[tail]] = tail

        if longestSize > len(hashedString):
            return longestSize
        return len(hashedString)

