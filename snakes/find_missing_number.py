# https://leetcode.com/problems/missing-number/
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # For any nums, we must have 0 -> len(nums)

        numset = set(nums)
        for i in range(0, len(nums) + 1):
            if i not in numset:
                return i

