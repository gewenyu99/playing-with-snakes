def bruteforce(n):
    n = sorted(n) #nlongn
    combinations = []
    tallest = []
    for i in range(1, 2**(len(n))):
        combinations.append(getBits(i, len(n)))

    for i in range(0, len(combinations)):
        combination = []
        for included in range(0, len(combinations[i])):
            if combinations[i][included]:
                combination.append(n[included])
        if(isValidCombination(combination)):
            if len(tallest) < len(combination):
                tallest = combination

    return tallest

def isValidCombination(combination):
    for i in range(0, len(combination) - 1):
        if not combination[i][0] <= combination[i+1][0] or not combination[i][1] <= combination[i+1][1]:
            return False
    return True



def getBits(num, bitLength):
    return [(num >> x) & 1 for x in range(0, bitLength)]

print(bruteforce([[1,2],[3,4],[1,3],[3,5],[4,1],[2134,2],[2134,7]]))



def dynamicProgramming(n):
    n = sorted(n)  # nlongn
    tallest = []
    longestOfLengthN = {0: [n[0]]}

    for i in range(1, len(n)):
        longestAppend = 0
        longestAppendKey = 0
        for key, tower in longestOfLengthN.items():
            if n[i][1] > tower[len(tower) - 1][1] and len(tower) > longestAppend:
                longestAppend = len(tower)
                longestAppendKey = key

        longestOfLengthN[i] = longestOfLengthN[longestAppendKey] + [n[i]]

    for key, tower in longestOfLengthN.items():
        if len(tower) > len(tallest):
            tallest = tower
    return tallest

print(dynamicProgramming([[1,2],[3,4],[1,3],[3,5],[4,1],[2134,2],[2134,7]]))