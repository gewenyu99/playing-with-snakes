# https://leetcode.com/problems/candy/description/ <-- this one
class Solution:
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
#       The first thing we'll have to do, is  find local max min
#       ya' know, like in calculus
        max = []
        min = []
        # These min maxes are actually sorted
        prevSlope = 0
        index = 0
        loc = "loc"
        lh = "leftHeight"
        rh = "rightHeight"
        lm = "leftMin"
        rm = "rightMin"
        retArr = [1] * len(ratings)

        if(len(ratings) == 1):
            return 1


        while ratings[index + 1] - ratings[index] == 0:
            index += 1
            if not index + 1 < len(ratings):
                retSum = 0
                for l in range(0, len(retArr)):
                    retSum += retArr[l]
                return retSum

        prevSlope = ratings[index + 1] - ratings[index]
        if prevSlope < 0:
            max.append({loc: index})
        else:
            min.append(index)
        index += 1
        while index + 1 < len(ratings):
            curSlope = ratings[index + 1] - ratings[index]
            if curSlope > 0 and prevSlope < 0:
                min.append(index)
            elif curSlope < 0 and prevSlope > 0:
                max.append({loc: index})
            if curSlope != 0:
                prevSlope = curSlope
            index += 1

        if prevSlope < 0:
            min.append(index)
        else:
            max.append({loc: index})

#       now we need to measure the height of each max
        i = 0
        j = 0
        while i < len(max) and j < len(min):
            if max[i][loc] < min[j]:
                tally = 0
                for k in range(max[i][loc], min[j]):
                    if ratings[k] != ratings[k + 1]:
                        tally += 1
                max[i][rh] = tally
                max[i][rm] = min[j]
                i += 1
            else:
                tally = 0
                for k in range(min[j], max[i][loc]):
                    if ratings[k] != ratings [k + 1]:
                        tally += 1
                max[i][lh] = tally
                max[i][lm] = min[j]
                j += 1
        if i < len(max):
            tally = 0
            for k in range(min[j - 1], max[i][loc]):
                if ratings[k] != ratings[k + 1]:
                    tally += 1
            max[i][lh] = tally
            max[i][lm] = min[j - 1]
            j += 1
        elif j < len(min):
            tally = 0
            for k in range(max[i - 1][loc], min[j]):
                if ratings[k] != ratings[k + 1]:
                    tally += 1
            max[i - 1][rh] = tally
            max[i - 1][rm] = min[j]
            i += 1
#       now we have our heights, we'll fill in the ret arr
#       We'll start at each min, because we're minimizing # of candy.
#       We already know the height of each max
#         print(min)
#         print(max)
        i = 0
        j = 0
        for i in range(0, len(max)):
            if lh in max[i] and rh in max[i]:
                retArr[max[i][loc]] += (max[i][lh]) if max[i][lh] >= max[i][rh] else (max[i][rh])
            else:
                retArr[max[i][loc]] += (max[i][lh]) if lh in max[i] else (max[i][rh])
            if not (lm in max[i]):
                for j in range(0, max[i][loc]):
                    retArr[j] = retArr[max[i][loc]]
                count = 0
                for k in range ((max[i][rm] if rm in max[i] else len(retArr) - 1), max[i][loc], -1):
                    retArr[k] += count
                    if ratings[k - 1] != ratings[k]:
                        count += 1
            else:
                count = 0
                for k in range(max[i][lm], max[i][loc]):
                    retArr[k] += count
                    if ratings[k + 1] != ratings[k]:
                        count += 1
            if not (rm in max[i]):
                for j in range(max[i][loc], len(retArr)):
                    retArr[j] = retArr[max[i][loc]]
                count = 0
                for k in range((max[i][lm] if lm in max[i] else 0), max[i][loc]):
                    retArr[k] += count
                    if ratings[k] != ratings[k + 1]:
                        count += 1
            else:
                count = 0
                for k in range(max[i][rm], max[i][loc], -1):
                    retArr[k] += count
                    if ratings[k - 1] != ratings[k]:
                        count += 1

        retSum = 0
        for l in range(0, len(retArr)):
            retSum += retArr[l]
        return retSum

#test1
print(Solution().candy([1,1,2,3,55,54,5,4,3,2,1,1,2,3,1,2]))
#test2
print(Solution().candy([1,2,2]))
#test3
print(Solution().candy([1]))
#test4
print(Solution().candy([2,1]))
#test5
print(Solution().candy([1,2]))
#test6
print(Solution().candy([1,1,2,3]))
#test7
print(Solution().candy([4,2,1]))
#test8
print(Solution().candy([1,2,3,4,5,6,4,2]))
#test9
print(Solution().candy([1,2,1]))
#test10
print(Solution().candy([1,2,3,4,5,1,2,3,5,123,432,12,4,5,1,2,3,54,2]))
#test11
print(Solution().candy([1,1,22,2,2,2,2,3,1,2,1,1,1,1,1,1,1,2,54,53,52,12,21,2]))


