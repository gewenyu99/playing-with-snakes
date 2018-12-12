# https://leetcode.com/problems/house-robber-ii/
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        prevPair = [0] * 2  # rob, norob
        prevPair2 = [0] * 2
        for i in range(0, len(nums) - 1):
            prevPair = nums[i] + prevPair[1], max(prevPair)
        for i in range(1, len(nums)):
            prevPair2 = nums[i] + prevPair2[1], max(prevPair2)

        return max(prevPair + prevPair2)