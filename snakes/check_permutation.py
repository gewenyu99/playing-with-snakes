class Solution:
    def isPermutation(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: bool
        """
#       This came from CTCI
#       For two nums to be permutations of one another, we'd need the same character set
#       As long as this is true, it is valid. This solution is O(N) in memory and run time

        if len(a) != len(b):
            return False

        if not a or not b:
            return False

        countingHash = {}
        for i in range(0, len(a)):
            if a[i] in countingHash:
                countingHash[a[i]] += 1
            else:
                countingHash[a[i]] = 1

        for i in range(0, len(b)):
            if b[i] in countingHash:
                countingHash[b[i]] -= 1
                if countingHash[b[i]] < 0:
                    return False
            else:
                return False



        return True

class TestSolution:
    def __init__(self):
        self.solution = Solution()

    def beginTest(self):
        a = ""
        b = ""
        print("input: " + a + ", " + b + " ==> returns:" + str(self.theTest(a,b)))
        a = "1"
        b = ""
        print("input: " + a + ", " + b + " ==> returns:" + str(self.theTest(a, b)))
        a = "a"
        b = "b"
        print("input: " + a + ", " + b + " ==> returns:" + str(self.theTest(a, b)))
        a = "aaaa"
        b = ""
        print("input: " + a + ", " + b + " ==> returns:" + str(self.theTest(a, b)))
        a = "abc"
        b = "bax"
        print("input: " + a + ", " + b + " ==> returns:" + str(self.theTest(a, b)))
        a = "bac"
        b = "abc"
        print("input: " + a + ", " + b + " ==> returns:" + str(self.theTest(a, b)))
        a = "1235"
        b = "53212"
        print("input: " + a + ", " + b + " ==> returns:" + str(self.theTest(a, b)))
        a = "1235"
        b = "5321"
        print("input: " + a + ", " + b + " ==> returns:" + str(self.theTest(a, b)))
        a = "aa  bb"
        b = "aabb  "
        print("input: " + a + ", " + b + " ==> returns:" + str(self.theTest(a, b)))

    def theTest(self, a, b):
        return self.solution.isPermutation(a,b)


TestSolution().beginTest()










