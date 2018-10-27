class Solution:
    def to_url(self, str, size):
        """
        :type str: string
        :type size: int
        :rtype: bool
        """
#       Replace spaces with %20 => came out of CTCI
#       Approach, run through character by character recursively
#       return either %20 or the cur char to the last char
#       append each time recursive function returns
#       Can do in place if we do string shifting, but is slower at O(Nlog(N))
#       or really hard to read

        return self.replaceSpace(str, 0, size)
    def replaceSpace(self, curString, count, size):
        if count >= size:
            return curString
        if curString[0] == ' ':
            return '%20' + self.replaceSpace(curString[1:], count + 1, size)
        else: return curString[0] + self.replaceSpace(curString[1:], count + 1, size)

class TestSolution:
    def __init__(self):
        self.solution = Solution()

    def beginTest(self):
        print(self.theTest("a b c      ", 5))
        print(self.theTest("        ", 5))
        print(self.theTest("a b c              ", 7))
        print(self.theTest("a", 1))
        print(self.theTest(" a   ", 2))
        print(self.theTest("    ", 1))



    def theTest(self, str, size):
        return self.solution.to_url(str, size)


TestSolution().beginTest()










