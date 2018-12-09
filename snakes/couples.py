# https://leetcode.com/problems/couples-holding-hands/description/ < thisone

class Solution(object):
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int

        So many couples, and it's always even so they've all got someone.
        This all lowkey makes me very sad
        """

        def couples(p1, p2):
            return partner(p1) == p2

        def swap(a, b):
            posA = hash_row[a]
            posB = hash_row[b]

            temp = row[posA]
            row[posA] = row[posB]
            row[posB] = temp
            hash_row[a] = posB
            hash_row[b] = posA

        def partner(person):
            if person % 2:
                return person - 1
            else:
                return person + 1

        swap_count = 0
        # We hash all the couples
        hash_row = {}
        for i in range(0, len(row)):
            hash_row[row[i]] = i


        for j in range(0, int(len(row)/2)):
            if not couples(row[j*2], row[j*2+1]):
                swap(row[j*2+1], partner(row[j*2]))
                swap_count += 1

        return swap_count




print(Solution().minSwapsCouples([5,6,4,0,2,1,9,3,8,7,11,10]))