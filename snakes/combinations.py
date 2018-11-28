# https://leetcode.com/problems/combinations/description/
class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        ret = []

        def recur(used, start):
            if len(used) == k:
                ret.append(used)
            else:
                for i in range(start, n + 1):
                    _used = used[:]
                    _used.append(i)
                    recur(_used, i + 1)

        recur([], 1)

        return (ret)
