# https://leetcode.com/problems/array-of-doubled-pairs/description/
class Solution(object):
    def canReorderDoubled(self, A):
        """
        Basically if it can be a palindrom after abs every value
        :type A: List[int]
        :rtype: bool
        """
        hashA = {}

        for i in range(0, len(A)):
            A[i] = abs(A[i])

        A.sort(reverse=True)

        for num in A:
            if num * 2 in hashA:
                hashA[num * 2] -= 1
                if not hashA[num * 2]:
                    del hashA[num * 2]
            else:
                if num in hashA:
                    hashA[num] += 1
                else:
                    hashA[num] = 1

        return not hashA