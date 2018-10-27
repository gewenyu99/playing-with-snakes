class Solution:
    def one_away(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: bool
        """
#       1.5 of CTCI
#       The key here, is to identify inset, remove, replace operations accurately
#       Ket identifier is length, which gives us the following freebies
#       Solution is O(N) in run time and O(1) in memory use
        if abs(len(a) - len(b)) > 1:
            return False
        # Now if the lengths are different, look for removes or adds
        elif len(a) != len(b):
            editCount = 0
            aCursor = 0
            bCursor = 0
            while aCursor < len(a) and bCursor < len(b):
                if a[aCursor] == b[bCursor]:
                    aCursor += 1
                    bCursor += 1
                elif editCount != 0:
                    editCount += 1
                    if aCursor + 1 < len(a) and a[aCursor + 1] == b[bCursor]:
                        aCursor + 2
                        bCursor + 1
                    elif bCursor + 1 < len(b) and a[aCursor] == b[bCursor + 1]:
                        aCursor + 1
                        bCursor + 2
                    else:
                        return False
                else:
                    return False

            while aCursor < len(a):
                editCount += 1
                aCursor += 1
            while bCursor < len(b):
                editCount += 1
                bCursor += 1
            if editCount != 1:
                return False
        else:
            editCount = 0
            for i in range(len(a)):
                if a[i] != b[i]:
                    editCount += 1
                    if editCount > 1:
                        return False
        return True

class TestSolution:
    def __init__(self):
        self.solution = Solution()

    def beginTest(self):
        print(self.theTest("aacccd","aaccc"))
        print(self.theTest("aa", ""))
        print(self.theTest("a", "b"))
        print(self.theTest("aacccd", "aacbcd"))
        print(self.theTest("aaccc", "aacccd"))
        print(self.theTest("cccc", "ccc"))
        print(self.theTest("cccc", "cccd"))
        print(self.theTest("ccac", "cccd"))
        return



    def theTest(self, a, b):
        return self.solution.one_away(a, b)



TestSolution().beginTest()










