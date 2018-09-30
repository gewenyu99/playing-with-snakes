# This is the solution to
# https://leetcode.com/problems/max-increase-to-keep-city-skyline/
class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # Here's my thought process
        #     1. We need to identfy the tallest of each col, row
        #     2. store this information
        #     3. look up to construct the new skyline
        rowMax = [0]*len(grid[0])
        colMax = [0]*len(grid)
        maxSumHeight = 0
        for i in range(0, len(grid)): #col
            for j in range(0, len(grid[i])): #row
                curHeight = grid[i][j]
                if curHeight > rowMax[j]:
                    rowMax[j] = grid[i][j]
                if curHeight > colMax[i]:
                    colMax[i] = grid[i][j]

        retGrid = [[0]*len(grid) for i in range(0, len(grid[0]))]

        for i in range(0, len(grid)): #col
            for j in range(0, len(grid[i])): #row
                maxSumHeight += (self.compare(rowMax[j], colMax[i]) - grid[j][i])
        return maxSumHeight

    def compare(self, a, b):
        if a >= b:
            return b
        else:
            return a
