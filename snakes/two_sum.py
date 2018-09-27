# solution to: https://leetcode.com/accounts/login/?next=/problems/two-sum/description/
# one pass hash map

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numDict = {}
        for num in enumerate(nums):
            numDict[num[1]] = num[0]
            if (target - num[1]) in numDict and (num[1] - target - num[1] != 0):
                return [numDict[target - num[1]], num[0]]



sol = Solution()
print(sol.twoSum([1,3,2,4],3))