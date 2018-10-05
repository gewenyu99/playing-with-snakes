# https://leetcode.com/problems/median-of-two-sorted-arrays
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        """
        while it is probable to do this problem with a two pointer approach
        it is also extremely messy and complicated to write, at least in my eye.
        I will instead do a merge first and find median normally
        """

        mergedArr = [0] * (len(nums1) + len(nums2))
        cur1 = 0
        cur2 = 0
        curMerged = 0

        while (cur1 < len(nums1) and cur2 < len(nums2)):
            if nums1[cur1] < nums2[cur2]:
                mergedArr[curMerged] = nums1[cur1]
                curMerged += 1
                cur1 += 1
            else:
                mergedArr[curMerged] = nums2[cur2]
                curMerged += 1
                cur2 += 1

        while (cur1 < len(nums1)):
            mergedArr[curMerged] = nums1[cur1]
            curMerged += 1
            cur1 += 1

        while (cur2 < len(nums2)):
            mergedArr[curMerged] = nums2[cur2]
            curMerged += 1
            cur2 += 1

        totLen = len(nums1) + len(nums2)
        if totLen % 2:
            # decrement by 1 because indexed from 0
            return mergedArr[int((totLen + 1) / 2 - 1)]
        else:
            return (mergedArr[int((totLen) / 2) - 1] + mergedArr[int((totLen) / 2 + 1) - 1]) / 2.0