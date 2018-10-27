class Solution:
    def strRotation(self, str1, str2):
        """
        :type str1: string
        :type str2: int
        :rtype: bool
        """
#       Sees if strings are a rotation of one another
#       eg "abcdefg" and "defgabc"
        if not (len(str1) or len(str2)):
            return False

        if len(str1) != len(str2):
            return False
        #Start with first character of str1 and search for it in str2
        initChar = str1[0]
        initIndex = 0 # will replace this with the index of initChar in str2

        while(str2[initIndex] != initChar):
            initIndex += 1
            if initIndex == len(str2):
                return False #This case is if they don't even have the same characters
        # here initIndex is found
        # We need to be looping through the two circularly

        for i in range(0, len(str1)):
            if str1[i] == str2[initIndex]:
                initIndex += 1
                if initIndex == len(str2):
                    initIndex = 0
            else:
                return False

        return True # if it didn't return previously is a rotation



class TestSolution:
    def __init__(self):
        self.solution = Solution()

    def beginTest(self):
        self.theTest("123", "231");
        self.theTest("123", "321");
        self.theTest("", "231");
        self.theTest("", "");
        self.theTest("1", "1");
        self.theTest("123", "2341");
    def theTest(self, str1, str2):
        print(self.solution.strRotation(str1, str2))




TestSolution().beginTest()










