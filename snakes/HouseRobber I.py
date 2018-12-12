# https://leetcode.com/problems/house-robber/
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        prevPair = [0] * 2  # rob, norob
        for house in nums:
            prevPair = house + prevPair[1], max(prevPair)

        return max(prevPair)