# solution to: https://leetcode.com/problems/longest-palindromic-substring
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        There are two types of palindromes;
        even palindromes
        odd palindromes

        We will check for the defining characteristics of both
        starting from the middle of the palindromes outwards

        This centre out approach should be around n^2 run time and memory use is basically (modified slightly) constant
        """

        # error checking
        if len(s) < 1:
            return ""
        if len(s) < 2:
            return s

        longestPalindrome = ""

        # check for odd palindrome
        for i in range(0, len(s)):
            symIndex = 0
            curLen = 1
            while (
                    i - symIndex <= 0
                    and i + symIndex < len(s)
            ):
                if s[i - symIndex] == s[i + symIndex]:
                    curLen += 1
                    if curLen > len(longestPalindrome):
                        longestPalindrome = s[i - symIndex: i + 1 + symIndex]
                    symIndex += 1
                else:
                    break

        # check for even palindrome
        for i in range(0, len(s)):
            symIndex = 0
            curLen = -1
            while (
                    i - symIndex >= 0
                    and i + symIndex < len(s)
            ):
                if s[i - symIndex] == s[i + symIndex]:
                    curLen += 2
                    if curLen > len(longestPalindrome):
                        longestPalindrome = s[i - symIndex: i + 1 + symIndex]
                    symIndex += 1
                else:
                    break
        for i in range(0, len(s)):
            symIndex = 0
            curLen = 0
            while (
                    i - symIndex >= 0
                    and i + symIndex + 1 < len(s)
                    # up index one because centre of
            ):
                if s[i - symIndex] == s[i + symIndex + 1]:
                    curLen += 2
                    if curLen > len(longestPalindrome):
                        longestPalindrome = s[i - symIndex: i + 2 + symIndex]
                    symIndex += 1
                else:
                    break

        return longestPalindrome