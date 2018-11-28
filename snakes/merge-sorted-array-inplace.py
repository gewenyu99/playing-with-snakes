class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """

        def shift(position):
            for i in range(len(nums1) - 1, position, -1):
                nums1[i] = nums1[i - 1]

        p1 = 0
        p2 = 0
        while p2 < n and p1 < m:
            if nums1[p1] <= nums2[p2]:
                p1 += 1
            else:
                shift(p1)
                nums1[p1] = nums2[p2]
                m += 1
                p1 += 1
                p2 += 1

        while p2 < n:
            nums1[p1] = nums2[p2]
            p2 += 1
            p1 += 1