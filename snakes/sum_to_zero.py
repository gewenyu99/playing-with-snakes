# This code contains solution to finding all sets of 3 int that sum to 0 in an array

class Solution:
    # This problem should take the following steps
    # 1. we wanna sort this stuff, I'm also lazy so List.sort() it is
    # 2. I wanna go through these values 1 by 1, refer to this as "item"
    # 3. I wanna find all the combinations of two nums that add to -item
    # 4. Ignore duplicates on the same item
    # 5. Ignore duplicates of item

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        returnList = []
        # Not editing a param directly, I just don't want to :')
        numsSorted = nums
        numsSorted.sort()
        #This bool is used to skip dups in first num
        nextNum = False

        for index, num in enumerate(numsSorted):
            if not nextNum:
                target = -num
                head = index + 1
                tail = len(numsSorted) - 1
                while head < tail:
                    sum = numsSorted[head] + numsSorted[tail]
                    if sum == target:
                        returnList.append([num, numsSorted[head], numsSorted[tail]])
                        # move head and tail to ignore duplicates
                        head += 1
                        while numsSorted[head] == numsSorted[head - 1] and head < tail:
                            head += 1
                        tail -= 1
                        while numsSorted[tail] == numsSorted[tail + 1] and head < tail:
                            tail -= 1
                    elif sum >= target:
                        tail -= 1
                        while numsSorted[tail] == numsSorted[tail + 1] and head < tail:
                            tail -= 1
                    else:
                        head += 1
                        while numsSorted[head] == numsSorted[head - 1] and head < tail:
                            head += 1
                # At this point we need to move index along to avoid duplicates.
            if index + 1 <= tail:
                nextNum = (numsSorted[index] == numsSorted[index + 1])

        return returnList


sol = Solution()
print(sol.threeSum([0,-4,-1,-4,-2,-3,2]))
