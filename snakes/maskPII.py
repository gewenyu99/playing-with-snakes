class Solution(object):
    def maskPII(self, S):
        """
        :type S: str
        :rtype: str
        """

        if '@' in S:
            return handleEmail(S)
        else:
            return handlePhone(S)


def handleEmail(s):
    maskedString = ''
    maskedString += s[0]
    maskedString += '*****'
    maskedString += s[findLastChar(s):]

    return maskedString.lower()

def handlePhone(s):
    s = s.replace('(', '')
    s = s.replace(')', '')
    s = s.replace(' ', '')
    s = s.replace('-', '')
    s = s.replace('+', '')

    if len(s) > 10:
        return '+' + buildAstr(len(s) - 10) + '-***-***-' + s[len(s) - 4:]
    return '***-***-' + s[len(s) - 4:]

def buildAstr(m):
    ret = ''
    for i in range (0, m):
        ret += '*'
    return ret

def findLastChar(s):
    for i in range(0, len(s)):
        if (s[i]) == '@':
            return i - 1



print(Solution().maskPII('ab.cD@gMail.com'))
print(Solution().maskPII('1(234)567-890'))